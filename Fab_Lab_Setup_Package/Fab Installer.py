import os, logging, gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

log_filename = 'Fab Installer.log'
log_format = '%(asctime)s %(levelname)s:%(message)s'
log_dateFormat = '%m/%d/%Y %H:%M %p'

logging.basicConfig(filename=log_filename,format=log_format, datefmt = log_dateFormat,level=logging.DEBUG)


class appWindow(Gtk.Window):
	
	def __init__(self):
		logging.info("Starting Fab Lab Installer.")
		Gtk.Window.__init__(self,title= 'Fab Lab Installer')
		
		grid = Gtk.Grid()
		self.add(grid)
		button1=Gtk.Button(label="Button 1")
		button2=Gtk.Button(label="Button 2")
		
		checkbutton = Gtk.CheckButton('Click Me')



		grid.add(button1)
		grid.attach(button2,1,0,2,1)
		grid.attach(checkbutton,4,0,2,1)

win = appWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()


def get_current_dir(self):
	main_dir = os.path.dirname(os.path.realpath(__file__))
	logging.info("Main Directory: %s", main_dir)

	print("Main Directory:" + main_dir)






