import os, logging, time, gi, platform
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

log_filename = 'Fab Installer.log'
log_format = '%(asctime)s %(levelname)s:%(message)s'
log_dateFormat = '%m/%d/%Y %H:%M %p'

logging.basicConfig(filename=log_filename,format=log_format, datefmt = log_dateFormat,level=logging.DEBUG)


class appWindow(Gtk.Window):


	def get_current_dir(self):
		main_dir = os.path.dirname(os.path.realpath(__file__))
		os_info = platform.dist()
		logging.info("Main Directory: %s", main_dir)
		logging.info("Operating System Information: %s", os_info)
		#print("Main Directory:" + main_dir)
		#print("Operating System Information: %s" , os_info)
		
	def get_user_pw(self, message, title=''):
	    # Returns user input as a string or None
	    # If user does not input text it returns None, NOT AN EMPTY STRING.
	    dialogWindow = Gtk.MessageDialog(self,
		                  Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
		                  Gtk.MessageType.QUESTION,
		                  Gtk.ButtonsType.OK_CANCEL,
		                  message)

	    dialogWindow.set_title(title)

	    dialogBox = dialogWindow.get_content_area()
	    userEntry = Gtk.Entry()
	    userEntry.set_visibility(False)
	    userEntry.set_invisible_char("*")
	    userEntry.set_size_request(250,0)
	    dialogBox.pack_end(userEntry, False, False, 0)

	    dialogWindow.show_all()
	    response = dialogWindow.run()
	    text = userEntry.get_text() 
	    dialogWindow.destroy()
	    if (response == Gtk.ResponseType.OK) and (text != ''):
			return text
	    else:
			return None

	def initate_installation(self, script):
		#userPassword = self.get_user_pw("Please enter your password", "Password")		
        command = "sudo apt-get update"
        os.system('echo %s|sudo -S %s' % (self.get_user_pw("Please enter your password", "Password"), command))
		#os.system("Sudo apt-get -y upgrade")

		# Install application dependencies 
		#os.system("Sudo apt-get -y install %s", pre requisites)

		#os.system("Sudo apt-get -y install %s", script)

# OnClick Actions
	def on_button_clicked(self, button, name):
		status = self.dict[name]	
		if(status):	
			 self.dict[name] = False
		else:
			self.dict[name] = True
		logging.debug("Installation Status for %s: %s", name, self.dict[name])

	def on_install_button_clicked(self, widget):		
		installScript=""
		logging.debug("Begin Installation. The Following programs will be installed:")
		for key, value in self.dict.items():
			if value:
				installScript += " "+ key
				print(installScript)
		self.initate_installation(installScript)			

	def __init__(self):
		logging.info("Starting Fab Lab Installer.")
		Gtk.Window.__init__(self,title= 'Fab Lab Installer')
		
		grid = Gtk.Grid()
		grid.set_row_spacing(2)

#Global Variables
		self.dict={'inkscape':False,'blender':False,'gimp':False,'cura':False,'makerbot':False,'fritzing':False,'fabModules':False,'eagle':False}
		# inkscape dependencies 
		# pstoedit

		# Libre-Office Plug-in dependencies 
		# python-tk cam.py laser.py tmp

		# Fab Modules Dependenceis
		# 
		
		header_label = Gtk.Label("Check the applications that should be installed:")
# Labels
		Inkscape_label = Gtk.Label("Inkscape 0.91")
		Blender_label = Gtk.Label("Blender")
		Gimp_label = Gtk.Label("Gimp")
		Cura_label = Gtk.Label("Cura")
		Makerbot_label = Gtk.Label("Makerbot")
		Fritzing_label = Gtk.Label("Fritzing")
		FabModules_label = Gtk.Label("Fab Modules")
		Eagle_label = Gtk.Label("Eagle")
# Buttons		
		Inkscape_checkbutton = Gtk.CheckButton()
		Blender_checkbutton = Gtk.CheckButton()
		Gimp_checkbutton = Gtk.CheckButton()
		Cura_checkbutton = Gtk.CheckButton()
		Makerbot_checkbutton = Gtk.CheckButton()	
		Fritzing_checkbutton = Gtk.CheckButton()
		FabModules_checkbutton = Gtk.CheckButton()
		Eagle_checkbutton = Gtk.CheckButton()

        Inkscape_checkbutton.connect("clicked", self.on_button_clicked,'inkscape')
        Blender_checkbutton.connect("clicked", self.on_button_clicked,'blender')
        Gimp_checkbutton.connect("clicked", self.on_button_clicked,'gimp')
        Cura_checkbutton.connect("clicked", self.on_button_clicked,'cura')
        Makerbot_checkbutton.connect("clicked", self.on_button_clicked,'makerbot')
        Fritzing_checkbutton.connect("clicked", self.on_button_clicked,'fritzing')
        FabModules_checkbutton.connect("clicked", self.on_button_clicked,'fabModules')
        Eagle_checkbutton.connect("clicked", self.on_button_clicked,'eagle')

        button1=Gtk.Button(label="Select All")
        install_button=Gtk.Button(label="Install")
        install_button.connect("clicked",self.on_install_button_clicked)

        self.add(grid)
# Set Location
        grid.add(header_label)
        grid.attach(Inkscape_label, 0, 1, 1, 2)	        
        grid.attach_next_to(Blender_label, Inkscape_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(Gimp_label, Blender_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(Cura_label, Gimp_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(Makerbot_label, Cura_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(Fritzing_label, Makerbot_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(FabModules_label, Fritzing_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(Eagle_label, FabModules_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button1, Eagle_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(install_button, button1, Gtk.PositionType.RIGHT, 1, 2)

        grid.attach_next_to(Inkscape_checkbutton, Inkscape_label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(Blender_checkbutton, Blender_label, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(Gimp_checkbutton, Gimp_label, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(Cura_checkbutton, Cura_label, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(Makerbot_checkbutton, Makerbot_label, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(Fritzing_checkbutton, Fritzing_label, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(FabModules_checkbutton, FabModules_label, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(Eagle_checkbutton, Eagle_label, Gtk.PositionType.RIGHT, 1, 2)

        self.get_current_dir()

win = appWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()









