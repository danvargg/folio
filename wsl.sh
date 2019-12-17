#!/bin/bash

# Update Ubuntu
sudo apt-get update && sudo apt-get upgrade

# Change to dir
cd /mnt/c/

# Download VScode
# https://code.visualstudio.com/

# Download git
# https://git-scm.com/download/win

# Run
# code .

# Setup .bashprofile

# Upgrade python


# Upgrade pip
sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall

# Install packages
python3 -m pip install <package>

#.sh file permission
chmon +x in.sh

# Change dir
. in.sh

#Setup bash profile
sudo vim  ~/.profile

#Copy .pem to ubuntu
cp innodem.pem /home/danvargg

#Key only readable by me
chmod 400 innodem.pem
