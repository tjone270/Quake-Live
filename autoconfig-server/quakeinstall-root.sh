#! /bin/bash
# quakeinstall-root.sh - quake live dedicated server installation for root user.
# intended to be run on a fresh VPS/Dedicated Server, this script must be run under the root user.
# created by Thomas Jones on 29/09/15.

if [ "$EUID" -ne 0 ]
  then echo "Please run under user 'root'."
  exit
fi
clear
echo "Updating 'apt-get'..."
apt-get update
clear
echo "Installing packages..."
apt-get -y install apache2 python3 python-setuptools lib32gcec1 curl nano samba build-essential python-dev unzip dos2unix mailutils wget
clear
echo "Installing ZeroMQ library..."
# we use '--without-libsodium' because I encounter many problems with trying to configure with it.
wget http://download.zeromq.org/zeromq-4.1.3.tar.gz; tar -xvzf zeromq-4.1.3.tar.gz; rm zeromq-4.1.3.tar.gz; cd zeromq*; ./configure --without-libsodium; make install; cd ..; rm -r zeromq*; easy_install pyzmq
clear
echo "Adding user 'qlserver'..."
useradd -m qlserver; usermod -a -G sudo qlserver; chsh -s /bin/bash qlserver; clear; echo "Enter the password to use for QLserver account:"; passwd qlserver
clear
# you might not want to do this: (it's a security risk, but makes things more convienient)
echo "Adding user 'qlserver' to sudoers file, and appending NOPASSWD..."
echo "qlserver ALL = NOPASSWD: ALL" >> /etc/sudoers
clear
echo "Stopping the Samba services..."
service smbd stop; service nmbd stop
clear
echo "Adding home directory sharing to Samba..."
echo -e "\n[homes]\n    comment = Home Directories\n    browseable = yes\n    read only = no\n    writeable = yes\n    create mask = 0755\n    directory mask = 0755" >> /etc/samba/smb.conf
clear
echo "Adding 'www' directory sharing to Samba..."
echo -e "\n[www]\n    comment = WWW Directory\n    path = /var/www\n    browseable = yes\n    read only = no\n    writeable = yes\n    create mask = 0755\n    directory mask = 0755" >> /etc/samba/smb.conf
clear
echo "Starting the Samba services..."
service smbd start; service nmbd start
clear
echo "Enter the password to use for user 'qlserver' in Samba:"
smbpasswd -a qlserver
clear
echo "Installing Supervisor..."
easy_install supervisor
clear
# this is now done in the quakeconfig.sh script, no need to create a config we won't be using.
#echo "Configuring Supervisor..."
#echo_supervisord_conf > /etc/supervisord.conf
#echo -e "\n[program:quakelive]\ncommand=/home/qlserver/quakestart.sh %(process_num)s\nuser=qlserver\nprocess_name=qzeroded_%(process_num)s\nnumprocs=10\nautorestart=true" >> /etc/supervisord.conf
#clear
echo "All work done for 'root' user, please login to 'qlserver'."
exit
