#!/bin/sh

###################################################################################
# David's Superb Fab Modules Installation Shell Script
# Created:     	   4/3/2014
# Original Author: David Solomon
#
# Last edited by: David Solomon
# Last edited on:  02/14/2015
# Summary: Installs all the packages and programs that are used in the Lab
#					for digital fabrication
# Verified Version: Ubuntu 12.xx, 14.04 LTS 
###################################################################################

echo "Info:  Start Fab Setup Installation" >> /var/log/Fab_setup.log


notify-send "Download Fab Modules"
echo "Debug:  Downloading Fab Modules" >> /var/log/Fab_setup.log

wget "http://kokompe.cba.mit.edu/fab_src.zip"

echo "Debug:  Create Fab Modules folder" >> /var/log/Fab_setup.log
sudo mkdir /opt/Fab\ Modules

echo "Debug:  Extracting the Files" >> /var/log/Fab_setup.log

notify-send "Extracting the Files"
sudo unzip fab_src.zip -d /opt/Fab\ Modules
sleep 5
echo "Debug:  Remove the Downloaded Zip File Fab_src" >> /var/log/Fab_setup.log
rm fab_src.zip

echo "Debug:  Installing Dependencies" >> /var/log/Fab_setup.log
notify-send "Installing Fab Modules Dependencies."
sudo apt-get install -y  python python-wxgtk2.8 python-dev python-pip gcc g++ libpng12-dev libgif-dev make bash okular libboost-thread-dev libboost-system-dev cmake
sudo pip install numpy PyOpenGL PyOpenGL_accelerate

set -e

notify-send "Using apt-get to install necessary packages"
sudo apt-get install -y libgtk2.0-dev freeglut3-dev libsdl1.2-dev libgstreamer-plugins-base0.10-dev libwebkitgtk-dev

cd ~
echo "Debug:  Downloading wxPython 3.0.0.0" >> /var/log/Fab_setup.log
notify-send "Downloading wxPython 3.0.0.0"
wget "http://downloads.sourceforge.net/wxpython/wxPython-src-3.0.0.0.tar.bz2"

echo "Debug:  Extracting wxPython and changing directories to wxPython-src-3.0.0.0" >> /var/log/Fab_setup.log
tar xvjf wxPython-src-3.0.0.0.tar.bz2
cd wxPython-src-3.0.0.0

cd wxPython
notify-send "Compiling wxPython 3.0.0.0"
echo "Debug: Compiling wxPython 3.0.0.0" >> /var/log/Fab_setup.log
sudo python build-wxpython.py --build_dir=../bld --install
notify-send "Updating library cache"
sudo ldconfig

echo "Debug:  Cleaning up" >> /var/log/Fab_setup.log
notify-send "Cleaning up"
cd ~
rm wxPython-src-3.0.0.0.tar.bz2
sudo rm -rf wxPython-src-3.0.0.0

notify-send "Testing:"
echo "Debug:  Testing wxPython" >> /var/log/Fab_setup.log
python -c "import wx; print 'wx version =', wx.version()"

sleep 5

echo "Debug:  Installing Fab Modules" >> /var/log/Fab_setup.log
notify-send " Installing Fab Modules"
cd /opt/Fab\ Modules/
sudo make fab
sudo make install
notify-send " Fab Modules Is installed "
echo "Debug:  Installation is Completed" >> /var/log/Fab_setup.log