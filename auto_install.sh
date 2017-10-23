#!/bin/sh
WORK_SPACE='./installation'

#upgrade
echo "Upgrading system"
#sudo apt-get update -y;
#sudo apt-get full-upgrade -y;

#install deps
echo "Installing deps"
#sudo apt-get install git python3.5 python-pip


#prepare work space
echo "Creating workspace"
mkdir WORK_SPACE
cd WORK_SPACE

#xtrlock+gesture support
echo "Do you want BetterXtrLock installed?(y/n)"
read LINE
if [ "$LINE" = "y" ];then
        echo "Downloading xtrlock from https://github.com/D0048/Better-XTrLock.git..."
        git clone https://github.com/D0048/Better-XTrLock.git
        cd Better-XTrLock
        #sh ./auto-install
        echo "This need to be compile manually according to https://github.com/D0048/Better-XTrLock"
        cd ..
else
        echo "Skip Xtrlock"
fi

echo "Installing python libs"
    sudo pip install -U numpy dhash pynput
