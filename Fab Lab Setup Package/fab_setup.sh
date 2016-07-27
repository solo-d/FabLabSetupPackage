#!/bin/sh

#######################################################################################################
# David's Superb Fab Lab Installation Shell Script
# Created:     	   11/15/2013
# Original Author: David Solomon
#
# Last edited by:  David Solomon
# Last edited on:  07/25/2016
# Summary: Installs all the packages and programs that are used in the Lab
#					for digital fabrication
# Verified Version: Ubuntu 12.xx, 14.04 LTS 
#######################################################################################################

echo "Info:  Start Fab Setup Installation" >> /var/log/Fab_setup.log
notify-send "Installing Update"

#######################################################################################################
# Update and Upgrade of Packages
#######################################################################################################

echo "Debug:  Get Update" >> /var/log/Fab_setup.log
	sudo apt-get -y update
echo "Debug:  Installing Upgrade" >> /var/log/Fab_setup.log
	sudo apt-get -y upgrade
	sudo apt-get -y dist-upgrade
	sudo apt-get -y install python-gi
echo "Debug:  Clean Up Packages" >> /var/log/Fab_setup.log
	sudo apt-get -y autoremove

# Call python Fab\ Installer.py




notify-send "Begin Plug-ins and Software Installation"
echo "Debug: Begin Plug-ins and Software Installation" >> /var/log/Fab_setup.log

#######################################################################################################

#######################################################################################################
# Installation of Plug-ins
#######################################################################################################

sudo apt-get -y install python-tk pstoedit libreoffice-base libreoffice-java-common cifs-utils \
flashplugin-installer gsfonts-x11 build-essential \
autoconf automake autopoint intltool libtool libglib2.0-dev libpng12-dev libgc-dev libfreetype6-dev \
liblcms1-dev libgtkmm-2.4-dev libxslt1-dev libboost-dev libpopt-dev libgsl0-dev libaspell-dev \
libpoppler-dev libpoppler-glib-dev 

#######################################################################################################

#######################################################################################################
# Installation of Standard Fab Lab Software  
#		Software that will be installed
#			-> Fritzing: 			An open-source hardware initiative that makes electronics accessible as a creative material for anyone. (http://fritzing.org/home/)
#			-> Inkscape: 		A professional quality vector graphics software.
#			-> Blender: 			Home of the open source 3D graphics and animation software.
#			-> Gimp: 				A free and open-source raster graphics editor used for image retouching and editing, free-form drawing,  resizing, cropping, 
#										photo-montages, converting between different image formats, and more specialized task.
#			-> Main-menu: 		An easy-to-use menu editor for GNOME that can add and edit new entries and menus. 
#			-> unzip:				An application that is used to unzip files.
#			-> vim:					An application for editing text.
#			-> Font manager:	Allows the user to easily install and remove fonts.
#			-> Eagle Cad:		A PCB Design Software.  (Not Supported as yet)
#			-> Cura:				Developed by Ultimaker to make 3D printing as easy and streamlined as possible.
#######################################################################################################

notify-send "Creating Fritzing Directory"
echo "Debug:  Create Fritzing folder" >> /var/log/Fab_setup.log
sudo mkdir /opt/Fritzing\ 0.9.1b 

notify-send "Downloading Fritzing Installation package"
echo "Debug:  Downloading Fritzing Installation package" >> /var/log/Fab_setup.log
wget http://fritzing.org/download/0.9.1b/linux-32bit/fritzing-0.9.1b.linux.i386.tar.bz2

notify-send "Extracting Fritzing Installation package"
echo "Debug:  Extracting Fritzing Installation package to /opt/Fritzing\ 0.9.1b " >> /var/log/Fab_setup.log
sudo tar xvjf fritzing-0.9.1b.linux.i386.tar.bz2 -C /opt/Fritzing\ 0.9.1b 
sudo rmdir -rf fritzing-0.9.1b.linux.i386.tar.bz2

#wget http://web.cadsoft.de/ftp/eagle/program/7.2/eagle-lin-7.2.0.run
#sudo sh eagle-lin-7.2.0.run

echo "Debug:  Installing inkscape, blender, gimp, main-menu, unzip, vim, and font-manager " >> /var/log/Fab_setup.log

# Installation of inkscape, blender, gimp, main-menu, unzip, vim, font-manager, and eagle 
sudo apt-get -y install alacarte blender gimp gimp-data gimp-plugin-registry gimp-data-extras inkscape unzip vim font-manager  

cd $SCRIPTDIR/Resources/
sleep 2

notify-send "Installing Cura For Ultimaker"
echo "Debug:  Installing Cura For Ultimaker " >> /var/log/Fab_setup.log
sudo apt-get -f install 
sudo dpkg -i cura_15.02.1-debian_i386.deb

# Find a way to dynamically get the latest version of http://software.ultimaker.com/current/Cura-2.1.2-Linux.deb

echo "Debug:  Installation of Fab Modules" >> /var/log/Fab_setup.log

# Installs Fab Modules application
cd $SCRIPTDIR
sleep 2
sudo chmod +x Fab_Modules_setup.sh
sudo ./Fab_Modules_setup.sh

#######################################################################################################

#######################################################################################################
# Setup Folders and Printers
#######################################################################################################

notify-send "Creating Users folder place holder on Desktop"
echo "Debug:  Creating Users folder place holder on Desktop" >> /var/log/Fab_setup.log
sudo mkdir /home/$USER/Desktop/Users

notify-send "Moving cam.py, cam_user.py, laser.py, and tmp to /usr/local/bin/fabscripts/"
echo "Debug:  Moving cam.py, cam_user.py, laser.py, and tmp to /usr/local/bin/fabscripts/" >> /var/log/Fab_setup.log

cd $SCRIPTDIR/Resources/
# Moves the files  need to print from the fab menu button to /usr/local/bin/fabscripts/
sudo mv fabscripts /usr/local/bin/

echo "Debug:  Creating the printers for the laser cutter" >> /var/log/Fab_setup.log

sudo /usr/sbin/lpadmin -p rawlaser -E -v lpd://192.168.50.101/queue -o printer-error-policy="abort-job"

sudo /usr/sbin/lpadmin -p rawlaser2 -E -v lpd://192.168.50.102/queue -o printer-error-policy="abort-job"

sudo /usr/sbin/lpadmin -p vinyl -E -v usb://Roland/GX-24?serial=CX84502 -o printer-error-policy="abort-job" 

#cp /home/fab/Desktop/Fab\ Lab\ Set\ Up\ Package/Fab\ Lab\ Resources/Read\ Me /home/fab/Desktop/

echo "Debug:  Make certain programs search able and executable and setup Users folder" >> /var/log/Fab_setup.log
sudo python Configure_fab.py -s y -i 192.168.50.99

sleep 5

echo "Debug:  Mounting drive and do final config" >> /var/log/Fab_setup.logsss
sudo mount -a

#######################################################################################################

#######################################################################################################
# Final Tweaks
#######################################################################################################

#copy background from folder to wallpaper folder
cp $SCRIPTDIR/Resources/fablab_wallpaper.png /usr/share/backgrounds/

gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/fablab_wallpaper.png

#add fonts
sudo mv /Resources/Fonts/* /usr/share/fonts/truetype/freefont/

notify-send "Change ownership, group and permission of the folder to current user"
echo "Debug:  Change ownership, group and permission of the folder to current user" >> /var/log/Fab_setup.log
# Changes ownership of the folder to the current user name 
sudo chown $USER -R /usr/local/bin/

# Changes the permission of read/write/execute (r/w/x/) of the file/folder 
sudo chmod 777 -R /usr/local/bin/

# Changes ownership of the folder to the current user name 
sudo chgrp -R users /usr/local/bin/

# Disable Shopping suggestions 
# gsettings set com.canonical.Unity.Lenses disabled-scopes “[‘more_suggestions-amazon.scope’, ‘more_suggestions-u1ms.scope’, ‘more_suggestions-populartracks.scope’, ‘music-musicstore.scope’, ‘more_suggestions-ebay.scope’, ‘more_suggestions-ubuntushop.scope’, ‘more_suggestions-skimlinks.scope’]”

sudo apt-get remove unity-lens-shopping

echo "Info:  Setup Complete" >> /var/log/Fab_setup.log
notify-send "Restart Computer to Complete Installation"

#sudo rmdir -rf Fab\ Lab\ Set\ Up\ Package/
