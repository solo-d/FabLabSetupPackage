#! /usr/bin/python
# Author: David Solomon
# Date: 2-9-2015
# Edited by: David Solomon 
# Date: 5-12-2015
# South End Technology Center @ Tent City

import sys, os, logging, getpass, getopt, re

"""
Usage: 

"""

#############################################################
#APT-GET NECESSARY PROGRAMS
#apt-get (-y = assume but yes - don't force if security risk)
#############################################################

def overwriteFile(filename, listLines):
	logging.debug ("%s accessiblity: readable = %s writeable = %s" % (filename, os.access(filename, os.R_OK),os.access(filename, os.W_OK)))
	if(os.path.exists(filename)):
		if(os.access(filename, os.W_OK)):
			logging.debug("Deleting '%s'." ,filename)
			os.remove(filename)
			logging.debug("File Removed: %s." % (not(os.path.exists(filename))))
			writeFile(filename, listLines)
		else:
			print("%s is not writeable" % (filename))
			logging.error("%s is not writeable",filename)
	else:
		logging.debug("%s does not exists: Going to create %s" % (filename,filename))
		writeFile(filename, listLines)

def writeFile(filename, listLines):
	logging.debug("writing %s." %(filename))
	_file = open(filename,"a")
	for line in listLines:
		_file.write(line+"\n")
	_file.close()

def Make_Cam_Executable():
	Application_folder = "/usr/share/applications/cam.desktop"
	Cam_Execute_Application_lines = ["[Desktop Entry]","Name=Cam","GenericName=Cam",
	"Comment=The is a application designed by Neil Gershenfeld to send digital image files to a computer controlled machine",
    "Exec=python /usr/local/bin/fabscripts/cam_user.py","Icon=/opt/Fab\ Modules/src/apps/cba_icon.png","Terminal=false",
    "Type=Application","StartupNotify=false"]
    logging.debug("writing %s to %s", Cam_Execute_Application_lines, Application_folder)
    overwriteFile(Application_folder, Cam_Execute_Application_lines)

def Make_Fab_Executable():
	Application_folder = "/usr/share/applications/fab.desktop"
	Fab_Execute_Application_lines = ["[Desktop Entry]","Name=Fab Modules","GenericName=Fab Modules",
	"Comment=The is a application designed by Neil Gershenfeld to send digital image files to a computer controlled machine",
    "Exec=fab","Icon=/opt/Fab\ Modules/src/apps/cba_icon.png","Terminal=false",
    "Type=Application","StartupNotify=false"]
    logging.debug("writing %s to %s", Fab_Execute_Application_lines, Application_folder)
    overwriteFile(Application_folder, Fab_Execute_Application_lines)

def Make_Fritzing_Executable():
	Application_folder = "/usr/share/applications/fritzing.desktop"
	Fritzing_Execute_Application_lines = ["[Desktop Entry]","Name=Fritzing", "GenericName=Fritzing",
	"Comment=Electronic Design Automation software",
    "Exec=/opt/Fritzing\ 0.9.1b/fritzing-0.9.1b.linux.i386/./Fritzing","Icon=/opt/Fab\ Modules/src/apps/cba_icon.png",
    "Terminal=false","Type=Application","Categories=Development;IDE;Electronics;"]
    logging.debug("writing %s to %s", Fritzing_Execute_Application_lines, Application_folder)
    overwriteFile(Application_folder, Fritzing_Execute_Application_lines)

def mount_users_folder(_ip):
	fstab_location = "/etc/fstab"
	fstab_lines = ["//"+_ip+"/Users   /home/"+getpass.getuser()+"/Desktop/Userscifs  guest,uid=1000,iocharset=utf8  0  0"]
	logging.debug("writing %s to %s" ,fstab_lines, fstab_location)
	writeFile(fstab_location, fstab_lines)

def init(argv):
    logging.basicConfig(filename='/var/log/Configure_fab.log',format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %I:%M:%S %p',level=logging.DEBUG)
    logging.info("")
    logging.info(' ~~~~~~~~~~~~~ Log File For Configure_fab.py ~~~~~~~~~~~~~ ')

    Make_Cam_Executable()
    Make_Fab_Executable()
    Make_Fritzing_Executable()

    mountShare = ''
    ip_addr =''
    try:
        opts, args = getopt.getopt(argv,"hs:i:",["share=","ip="])
    except getopt.GetoptError:
        print ('Configure_fab.py -s < y / n > -i < Server ip address >')
        print ('Configure_fab.py --share < y / n > --ip < Server ip address >')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-s", "--share"):
            mountShare = arg
        elif opt in ("-i", "--ip"):
            ip_addr = arg
    match = re.search('^[y]', mountShare)
    if match is not None:
        if match.group(0) == "y":
            mount_users_folder(ip_addr)

###############################################
#START OF MAIN PROGRAM
###############################################

#initialize variables
init(sys.argv[1:])