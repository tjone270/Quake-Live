# qlping

A command-line utility for pinging Quake Live game servers using the Valve Source Query Protocol, in a manner very similar to the built-in `ping` tool available on most operating systems.

## Overview

`qlping` measures the round-trip time (RTT) between your computer and Quake Live servers, helping you assess server responsiveness and network quality. Unlike standard ICMP ping, this tool uses the same UDP protocol that Quake Live uses, providing a more accurate representation of in-game latency.

## Installation

Simply download `qlping.exe` and run it from the command line. No installation required.

## Usage

```
qlping [OPTIONS] <ADDRESS>
```

### Basic Examples

```bash
# Ping a server using default port (27960)
qlping 192.168.1.100

# Ping a server with custom port
qlping 192.168.1.100:27961

# Ping using hostname
qlping myserver.example.com:27960

# Send 10 pings
qlping -c 10 192.168.1.100

# Ping with 2-second interval
qlping -i 2 192.168.1.100
```

### Options

- `-c, --count <COUNT>` - Number of packets to send (default: continuous)
- `-i, --interval <SECONDS>` - Interval between packets in seconds (default: 1, minimum: 1)
- `-t, --timeout <SECONDS>` - Timeout for each packet in seconds (default: 2)
- `-q, --query <TYPE>` - Query type to use: `info` or `ping` (default: info)
- `-h, --help` - Display help information
- `-V, --version` - Display version information

### Query Types

- **info** (default) - Uses A2S_INFO query, the standard method for querying Source engine servers
- **ping** - Uses A2A_PING query (deprecated, no longer supported)

## Output

### Standard Output
```
PING 192.168.1.100 (192.168.1.100:27960) using A2S_INFO protocol
64 bytes from 192.168.1.100:27960: seq=1 time=12.457 ms
64 bytes from 192.168.1.100:27960: seq=2 time=11.923 ms
64 bytes from 192.168.1.100:27960: seq=3 time=13.102 ms
```

### Statistics Summary
After termination (Ctrl+C or completion), displays:
```
--- 192.168.1.100 ping statistics ---
10 packets transmitted, 10 received, 0.0% packet loss
rtt min/avg/max = 11.923/12.827/13.102 ms
```

## Notes

- Quake Live servers typically respond with a challenge (S2C_CHALLENGE) rather than direct info
- The measured RTT includes network latency plus server processing time
- Use Ctrl+C to stop continuous pinging and display statistics
- Default port 27960 is assumed if no port is specified
- All times are displayed in milliseconds (ms)

## Troubleshooting

**Request timeout** - Either the server may be offline, firewalled, in LAN mode or not responding to queries, or you are being blocked from contacting the server.

**Unexpected response type** - Server may not fully support the Source Query Protocol.

**High packet loss** - Check network connection or try increasing timeout with `-t`

## Exit Codes

- 0 - Success
- 1 - Error (invalid arguments, network failure, etc.)
