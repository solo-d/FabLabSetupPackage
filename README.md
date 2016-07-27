# FabLabSetupPackage
I am a Fab Lab Steward at Fab Lab Boston. In the past we never update our version of Ubuntu. Recently my self and a colleague of mine took over the Fab Lab. Since we have been there we upgrade all the pc to the latest version of Ubuntu. However, the process was manual. I hated it, so what did I do, I automated most of the terminal stuff so we don't have to sit there and type in hundreds of lines of code hoping we did not make a mistake or missed a step. My goal is to one day have the entire process automated and design this script to working for any Fab Lab that wants to run their lab off of Ubuntu

Fab Lab Setup Guide Rev 2.0
Author: David Solomon
Date: 2-21-2015
Revised Last by: David Solomon
Date: 5-19-2015

Disclaimer(s):
	This Fab Lab Setup Guide works with and was tested on Ubuntu 12.xx and 14.04 LTS on February 21, 2015
	This guide was designed for the computers at Fab Lab Boston but will work on other computers.
	The steps in this guide were not tested on Ubuntu 13.xx but should be compatible.
	Fab Lab Boston support Ubuntu 12.xx and 14.04 as of March 21, 2015
	Anything in [] means you have to type it into a text box
	Anything in {} Means search for it on Google or in a web browser


How to Setup Ubuntu in a Fab Lab

	1) Download Ubuntu 12.xx or 14.04 LTS and follow the instruction on how to make a boot-able disc or usb
		1a) It is highly recommended that you download the LTS version of Ubuntu Desktop
	2) If installing on a Mac 
		2a) Download reFIND Mac disk image from { http://sourceforge.net/projects/refind/ } 
			2a.1) This will start the Mac in the disk starter
				2a.1.a) Installation instructions { http://sourceforge.net/projects/refind/ }
			2a.2) Open the terminal
			2a.3) Change the directory so you are located in the reFIND folder then Type in ./install.sh
		2b) Create a new partition of free space. (A minimum of 20 gb is required for Ubuntu)
		2c) Insert the boot-able Ubuntu disc or usb now
		2c) Restart the computer. This should brings you to the startup manager or grub
		2d) Select the image that looks like a disc or usb and says Ubuntu
	3) Installing Ubuntu
		3a) Select Location 
		3b) Select Keyboard
		3c) Set your name: Example [Fab Lab]
		3d) Set the Computer name. Example [fabLab#]
		3e) Set the username. Example [fab]
		3f) Set your password (To make life easier set the same password for all the computers in the lab)
	4) To setup the user folder and laser-cutters Follow these steps
             [Setting up ubuntu]
		4a) Copy the folder named ' Fab Lab Set Up Package ' to the Desktop
		4b) Open the terminal and type in [ cd Desktop/Fab\ Lab\ Set\ Up\ Package/ ]
		4c) Next type in [ sudo chmod +x fab_setup.sh ]
		4d) Next type in [ sudo ./fab_setup.sh ]
		4e) Let it do its thing. When it is finished it will bring back the standard user prompt.
		
	5) The last step is to install the FabMenu Button in LibreOffice Draw
		5a) Open LibreOffice Draw
		5b) Go to the menu bar and scroll over to tool
		5c) Click on Extension Manager then click on add
		5d) Navigate to the desktop and open the folder LibreOfficePlugin and select  fabricate.zip and click open.
		5e) Restart LibreOffice Draw and make a simple test cut to ensure that the computer is able to print to both laser-cutters

Additional Setup steps
	1) Adding the Vinyl Cutter
		1a) Plug the Vinyl Cutter into the computer
		1b) Open System Settings and click on printers
		1c) Click on Add. The vinyl cutter should appear automatically as Roland ... 
		1d) Add it using the default settings. Change the name to [ vinyl ]

		1e) ~#~#~#~#~#~#~#~# To be added later #~#~#~#~#~#~#~#~#~#~




Ubuntu packages:
	Packages need for cam to work
		python-tk

	Packages need for the LibreOffice Plug-in to work
		pstoedit

	Packages for LibreOffice
		libreoffice-base 
		libreoffice-java-common

	Packages for File sharing  (Users folder)
		cifs-utils

	Packages for Flash Player in Firefox web browser
		flashplugin-installer gsfonts-x11

	Packages for Fab Modules
		wxPython 3.0.0.0
		python 
		python-wxgtk2.8 
		python-dev 
		python-pip 
		gcc 
		g++ 
		libpng12-dev 
		libgif-dev 
		make 
		bash 
		okular 
		libboost-thread-dev 
		libboost-system-dev 
		cmake
		numpy 
		PyOpenGL
		PyOpenGL_accelerate
		libgtk2.0-dev 
		freeglut3-dev 
		libsdl1.2-dev 
		libgstreamer-plugins-base0.10-dev 
		libwebkitgtk-dev

Ubuntu Software installation 
	Fritzing: 						An open-source hardware initiative that makes electronics accessible as a creative material for anyone. (http://fritzing.org/home/)
	Inkscape: 						A professional quality vector graphics software.
	Blender: 						Home of the open source 3D graphics and animation software.
	Gimp: 							A free and open-source raster graphics editor used for image retouching and editing, free-form drawing,  resizing, cropping, photo-montages, converting between different image formats, and more specialized task.
	Font manager:				Allows the user to easily install and remove fonts.
	Eagle Cad:					A PCB Design Software. 
	Cura:							Developed by Ultimaker to make 3D printing as easy and streamlined as possible.

  Dev Tools:
  	Alacarte (Main-menu): 	An easy-to-use menu editor for GNOME that can add and edit new entries and menus. 
	Unzip:							An application that is used to unzip files.
	Vim:								An application for editing text.

	

Important locations

usr/local/bin/* this is where fabscripts and fab modules files are kept.