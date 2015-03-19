#!/bin/sh

###################################################################################
# David's Superb Fab Lab Installation Shell Script
# Created:     	   11/15/2013
# Original Author: David Solomon
#
# Last edited by:  David Solomon
# Last edited on:  02/17/2015
# Summary: Installs all the packages and programs that are used in the Lab
#					for digital fabrication
# Verified Version: Ubuntu 12.xx, 14.xx 
###################################################################################

echo "Info:  Start Fab Setup Installation" >> /var/log/Fab_setup.log
notify-send "Installing Update"
# Update and upgrade of packages

echo "Debug:  Get Update" >> /var/log/Fab_setup.log
	sudo apt-get -y update
echo "Debug:  Installing upgrade" >> /var/log/Fab_setup.log
	sudo apt-get -y upgrade
	sudo apt-get -y dist-upgrade
echo "Debug:  Clean up packages" >> /var/log/Fab_setup.log
	sudo apt-get -y autoremove

notify-send "Begin plug-ins and Software Installation"
echo "Debug: Begin plug-ins and Software Installation" >> /var/log/Fab_setup.log

# Plug-ins
sudo apt-get -y install python-tk pstoedit libreoffice-base libreoffice-java-common cifs-utils \
flashplugin-installer gsfonts-x11 build-essential \
autoconf automake autopoint intltool libtool libglib2.0-dev libpng12-dev libgc-dev libfreetype6-dev \
liblcms1-dev libgtkmm-2.4-dev libxslt1-dev libboost-dev libpopt-dev libgsl0-dev libaspell-dev \
libpoppler-dev libpoppler-glib-dev 

notify-send "Creating Fritzing Directory"
echo "Debug:  Create Fritzing folder" >> /var/log/Fab_setup.log

sudo mkdir /opt/Fritzing\ 0.9.1b 

notify-send "Downloading Fritzing Installation package"
echo "Debug:  Downloading Fritzing Installation package" >> /var/log/Fab_setup.log

wget http://fritzing.org/download/0.9.1b/linux-32bit/fritzing-0.9.1b.linux.i386.tar.bz2
#wget http://web.cadsoft.de/ftp/eagle/program/7.2/eagle-lin-7.2.0.run

notify-send "Extracting Fritzing Installation package"
echo "Debug:  Extracting Fritzing Installation package to /opt/Fritzing\ 0.9.1b " >> /var/log/Fab_setup.log
sudo tar xvjf fritzing-0.9.1b.linux.i386.tar.bz2 -C /opt/Fritzing\ 0.9.1b 
sudo rmdir -rf fritzing-0.9.1b.linux.i386.tar.bz2

echo "Debug:  Installing inkscape, blender, gimp, main-menu, unzip, vim, font-manager, ekiga " >> /var/log/Fab_setup.log

# Installs inkscape, blender, gimp, main-menu, unzip, vim, font-manager, ekiga and eagle 
sudo apt-get -y install alacarte 	 	# This installs the application main menu which will be used to make cam an executable program
sudo apt-get -y install blender gimp gimp-data gimp-plugin-registry gimp-data-extras inkscape unzip vim font-manager ekiga 
#sudo sh eagle-lin-7.2.0.run

notify-send "Creating Fabscripts Directory"
echo "Debug:  Create Fabscripts folder" >> /var/log/Fab_setup.log
# Set up folder that will hold the cam and laser cutter python scripts
sudo mkdir /usr/local/bin/fabscripts

cd ~/Desktop/Fab\ Lab\ Set\ Up\ Package/usr-local-bin-fabscripts/
sleep 2

notify-send "Moving cam.py, cam_user.py, laser.py, and tmp to /usr/local/bin/fabscripts/"
echo "Debug:  Moving cam.py, cam_user.py, laser.py, and tmp to /usr/local/bin/fabscripts/" >> /var/log/Fab_setup.log

# Moves the files need to /usr/local/bin/fabscripts/
sudo mv cam.py /usr/local/bin/fabscripts/
sleep 2
sudo mv cam_user.py /usr/local/bin/fabscripts/
sleep 2
sudo mv laser.py /usr/local/bin/fabscripts/
sleep 2
sudo mv tmp /usr/local/bin/fabscripts/

notify-send "Change ownership and permission of the folder to fab"
echo "Debug:  Change ownership and permission of the folder to fab" >> /var/log/Fab_setup.log
# Changes ownership of the folder to fab
#sudo chown nobody.nogroup /usr/local/bin/fabscripts/*

sudo chown $USER /usr/local/bin/fabscripts/*

# Changes the permission of read/write/execute (r/w/x/) of the file/folder 
sudo chmod 755 /usr/local/bin/fabscripts/*

sudo mkdir /home/$USER/Desktop/Users

cd ..
sleep 2

echo "Debug:  Installs Fab Modules" >> /var/log/Fab_setup.log

# Installs Fab Modules
cd ~/Desktop/Fab\ Lab\ Set\ Up\ Package/
sleep 2
sudo chmod +x Fab_Modules_setup.sh
sudo ./Fab_Modules_setup.sh

echo "Debug:  Make certain programs search able and executable and setup Users folder" >> /var/log/Fab_setup.log
sudo python Configure_fab.py
#sudo rmdir -rf Fab\ Lab\ Set\ Up\ Package/

sleep 5

sudo mount -a
echo "Info:  Setup Complete" >> /var/log/Fab_setup.log
notify-send "Restart Computer to Complete Installation"