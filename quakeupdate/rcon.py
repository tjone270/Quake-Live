#!/usr/bin/env python

import sys
import time
import struct
import argparse
import uuid
import threading
import Queue

import logging
logging.basicConfig(level = logging.CRITICAL, format="%(message)s")

import zmq

import unittest

def _readSocketEvent( msg ):
    # NOTE: little endian - hopefully that's not platform specific?
    event_id = struct.unpack( '<H', msg[:2] )[0]
    # NOTE: is it possible I would get a bitfield?
    event_names = {
        zmq.EVENT_ACCEPTED : 'EVENT_ACCEPTED',
        zmq.EVENT_ACCEPT_FAILED : 'EVENT_ACCEPT_FAILED',
        zmq.EVENT_BIND_FAILED : 'EVENT_BIND_FAILED',
        zmq.EVENT_CLOSED : 'EVENT_CLOSED',
        zmq.EVENT_CLOSE_FAILED : 'EVENT_CLOSE_FAILED',
        zmq.EVENT_CONNECTED : 'EVENT_CONNECTED',
        zmq.EVENT_CONNECT_DELAYED : 'EVENT_CONNECT_DELAYED',
        zmq.EVENT_CONNECT_RETRIED : 'EVENT_CONNECT_RETRIED',
        zmq.EVENT_DISCONNECTED : 'EVENT_DISCONNECTED',
        zmq.EVENT_LISTENING : 'EVENT_LISTENING',
        zmq.EVENT_MONITOR_STOPPED : 'EVENT_MONITOR_STOPPED',
    }
    event_name = event_names[ event_id ] if event_names.has_key( event_id ) else '%d' % event_id
    event_value = struct.unpack( '<I', msg[2:] )[0]
    return ( event_id, event_name, event_value )

def _checkMonitor( monitor ):
    try:
        event_monitor = monitor.recv( zmq.NOBLOCK )
    except zmq.Again:
        #logging.debug( 'again' )
        return

    ( event_id, event_name, event_value ) = _readSocketEvent( event_monitor )
    event_monitor_endpoint = monitor.recv( zmq.NOBLOCK )
    logging.info( 'monitor: %s %d endpoint %s' % ( event_name, event_value, event_monitor_endpoint ) )
    return ( event_id, event_value )

# bunch of experiments that didn't go in the riht direction
class Test( unittest.TestCase ):
    def testPair( self ):
        timeline = time.time()
        
        HOST = 'tcp://127.0.0.1:27960'
        POLL_TIMEOUT = 1000
        
        server_ctx = zmq.Context()
        server_socket = server_ctx.socket( zmq.PAIR )

        monitor = server_socket.get_monitor_socket( zmq.EVENT_ALL )
        
        server_socket.bind( HOST )

        client_ctx_1 = zmq.Context()
        client_socket_1 = client_ctx_1.socket( zmq.PAIR )
        client_socket_1.connect( HOST )

        client_ctx_2 = zmq.Context()
        client_socket_2 = client_ctx_2.socket( zmq.PAIR )
        client_socket_2.connect( HOST )

        while ( True ):
            event = server_socket.poll( POLL_TIMEOUT )
            _checkMonitor( monitor )
            if ( time.time() - timeline > 4 ):
                break

        timeline = time.time()
        
        server_socket.send( 'console line 1' )
        server_socket.send( 'console line 2' )

        ev1 = client_socket_1.poll( POLL_TIMEOUT )
        ev2 = client_socket_2.poll( POLL_TIMEOUT )

        # won't sustain multiple peers ..
        logging.info( repr( [ ev1, ev2 ] ) )
        self.assertEqual( [ ev1, ev2 ], [ 1, 0 ] )

    def testMix( self ):
        HOST = 'tcp://127.0.0.1:27960'
        POLL_TIMEOUT = 1000
        
        server_ctx = zmq.Context()
        
        server_pub = server_ctx.socket( zmq.PUB )
        server_pub.bind( HOST )
        monitor_pub = server_pub.get_monitor_socket( zmq.EVENT_ALL )

        # yeah you can't
        server_rep = server_ctx.socket( zmq.REP )
        self.assertRaises( zmq.ZMQError, server_rep.bind, HOST )

    def testMulti( self ):
        timeline = time.time()
        
        HOST = 'tcp://127.0.0.1:27960'
        POLL_TIMEOUT = 1000
        
        server_ctx = zmq.Context()

        server_rep = server_ctx.socket( zmq.REP )
        server_rep.bind( HOST )
        monitor = server_rep.get_monitor_socket( zmq.EVENT_ALL )

        client_ctx_1 = zmq.Context()
        client_socket_1 = client_ctx_1.socket( zmq.REQ )
        client_socket_1.connect( HOST )

        client_ctx_2 = zmq.Context()
        client_socket_2 = client_ctx_2.socket( zmq.REQ )
        client_socket_2.connect( HOST )

        client_socket_1.send( 'req 1' )
        client_socket_2.send( 'req 2' )
        
        while ( True ):
            event = server_rep.poll( POLL_TIMEOUT )
            _checkMonitor( monitor )

            if ( time.time() - timeline > 4 ):
                break
            
            if ( event == 0 ):
                continue

            msg = server_rep.recv( zmq.NOBLOCK )
            logging.info( repr( msg ) )
            server_rep.send( 'ack' ) # REQ/REP always have to ack

# summarizes a working setup and details QL's implementation
# based on http://zguide2.zeromq.org/py%3aall#Asynchronous-Client-Server
class TestRcon( unittest.TestCase ):
    def test( self ):
        timeline = time.time()
        
        HOST = 'tcp://127.0.0.1:27960'
        POLL_TIMEOUT = 1000
        
        server_ctx = zmq.Context()
        server = server_ctx.socket( zmq.ROUTER )
        server.bind( HOST )

        client_ctx_1 = zmq.Context()
        client_socket_1 = client_ctx_1.socket( zmq.DEALER )
        client_socket_1.setsockopt( zmq.IDENTITY, 'client-1' )
        client_socket_1.connect( HOST )
        client_socket_1.send( 'hello' ) # first message is ignored and used to notify server of presence
        client_socket_1.send( 'do this' )

        client_ctx_2 = zmq.Context()
        client_socket_2 = client_ctx_2.socket( zmq.DEALER )
        client_socket_2.setsockopt( zmq.IDENTITY, 'client-2' )
        client_socket_2.connect( HOST )
        client_socket_2.send( 'hello' )
        client_socket_2.send( 'do that' )

        clients = []
        
        while ( True ):
            event = server.poll( POLL_TIMEOUT )
            if ( event == 0 ):

                if ( time.time() - timeline > 2 ):
                    # console output would blindly go to all connected clients
                    for id in clients:
                        server.send( id, zmq.SNDMORE )
                        server.send( 'console line 1' )
                    break
                
                continue

            client_id = server.recv()
            msg = server.recv()

            try:
                clients.index( client_id )
            except:
                logging.info( 'new client %s' % client_id )
                clients.append( client_id )
                continue

            logging.info( 'client %s sends command %s' % ( client_id, repr( msg ) ) )

        # read the console lines

        def pollClient( id, client ):
            event = client.poll( POLL_TIMEOUT )
            if ( event == 0 ):
                return

            msg = client.recv()
            logging.info( 'client %s: %s' % ( id, msg ) )

        pollClient( 'client-1', client_socket_1 )
        pollClient( 'client-2', client_socket_2 )

        # client 1 disconnects
        client_socket_1.close()

        monitor = server.get_monitor_socket( zmq.EVENT_ALL )
        
        server.send( 'client-1', zmq.SNDMORE )
        server.send( 'console line 2' )

        time.sleep( 1 )

        # we get EVENT_DISCONNECTED - and the endpoint in metadata
        # the server matches this to know which client is disconnected
        _checkMonitor( monitor )

# start a thread, read a queue that will read input lines
def setupInputQueue():
    def waitStdin( q ):
        while ( True ):
            l = sys.stdin.readline()
            q.put( l )
    q = Queue.Queue()
    t = threading.Thread( target = waitStdin, args = ( q, ) )
    t.daemon = True
    t.start()
    return q

class TestInput( unittest.TestCase ):
    @unittest.skip("requires interaction")
    def test( self ):
        while ( True ):
            logging.info( 'waiting on readline' )
            line = sys.stdin.readline()
            logging.info( 'input: %s' % repr( line ) )

    @unittest.skip("requires interaction")
    def testBGRead( self ):
        q = setupInputQueue()
        while ( True ):
            logging.info( 'sleep' )
            time.sleep( 0.5 )
            while ( not q.empty() ):
                l = q.get()
                logging.info( 'input: %s' % repr( l ) )

HOST = 'tcp://127.0.0.1:27961'
POLL_TIMEOUT = 100
DONE = False

if ( __name__ == '__main__' ):
    reply_buffer = ""
    logging.info( 'zmq python bindings %s, libzmq version %s' % ( repr( zmq.__version__ ), zmq.zmq_version() ) )
    parser = argparse.ArgumentParser( description = 'Verbose QuakeLive server statistics' )
    parser.add_argument( '--host', default = HOST, help = 'ZMQ URI to connect to. Defaults to %s' % HOST )
    parser.add_argument( '--password', required = False )
    parser.add_argument( '--identity', default = uuid.uuid1().hex, help = 'Specify the socket identity. Random UUID used by default' )
    parser.add_argument( '--command', required = True )
    args = parser.parse_args()
    # TODO: put a curses or a tk interface on top of this
    #q = setupInputQueue()
    try:
        ctx = zmq.Context()
        socket = ctx.socket( zmq.DEALER )
        monitor = socket.get_monitor_socket( zmq.EVENT_ALL )
        if ( args.password is not None ):
            logging.info( 'setting password for access' )
            socket.plain_username = 'rcon'
            socket.plain_password = args.password
            socket.zap_domain = 'rcon'
        socket.setsockopt( zmq.IDENTITY, args.identity )
        socket.connect( args.host )
        logging.info( 'Connecting to %s' % args.host )
        while not DONE:
            event = socket.poll( POLL_TIMEOUT )
            event_monitor = _checkMonitor( monitor )
            if ( event_monitor is not None and event_monitor[0] == zmq.EVENT_CONNECTED ):
                # application layer protocol - notify the server of our presence
                logging.info( 'Registering with the server.' )
                socket.send( 'register' )
                socket.send(args.command)
                def set_done():
                    global DONE
                    time.sleep(1.5)
                    DONE = True
                threading.Thread(target=set_done).start()
                
            if ( event == 0 ):
                continue

            while not DONE:
                try:
                    msg = socket.recv( zmq.NOBLOCK )
                except zmq.error.Again:
                    break
                except Exception as e:
                    logging.info( e )
                    break
                else:
                    reply_buffer += msg
                    if msg[-1] == "\n":
                        print( reply_buffer.strip() )
                        reply_buffer = ""
    except Exception as e:
        logging.info( e )
