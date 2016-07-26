import os, logging, gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

log_filename = 'Fab Installer.log'
log_format = '%(asctime)s %(levelname)s:%(message)s'
log_dateFormat = '%m/%d/%Y %H:%M %p'

logging.basicConfig(filename=log_filename,format=log_format, datefmt = log_dateFormat,level=logging.DEBUG)


class appWindow(Gtk.Window):

	def get_current_dir(self):
		main_dir = os.path.dirname(os.path.realpath(__file__))
		logging.info("Main Directory: %s", main_dir)
		print("Main Directory:" + main_dir)

	
	def __init__(self):
		logging.info("Starting Fab Lab Installer.")
		Gtk.Window.__init__(self,title= 'Fab Lab Installer')
		
		grid = Gtk.Grid()
		grid.set_row_spacing(2)
		self.add(grid)
		
		header_label = Gtk.Label("Check the applications that should be installed:")
		Inkscape_label = Gtk.Label("Inkscape 0.91")
		Blender_label = Gtk.Label("Blender")
		Gimp_label = Gtk.Label("Gimp")
		Cura_label = Gtk.Label("Cura")
		Makerbot_label = Gtk.Label("Makerbot")
		Fritzing_label = Gtk.Label("Fritzing")
		FabModules_label = Gtk.Label("Fab Modules")
		Eagle_label = Gtk.Label("Eagle")

		button1=Gtk.Button(label="Select All")
		button2=Gtk.Button(label="Install")
		
		Inkscape_checkbutton = Gtk.CheckButton('Click Me')
		Blender_checkbutton = Gtk.CheckButton('Click Me')
		Gimp_checkbutton = Gtk.CheckButton('Click Me')
		Cura_checkbutton = Gtk.CheckButton('Click Me')
		Makerbot_checkbutton = Gtk.CheckButton('Click Me')	
		Fritzing_checkbutton = Gtk.CheckButton('Click Me')
		FabModules_checkbutton = Gtk.CheckButton('Click Me')
		Eagle_checkbutton = Gtk.CheckButton('Click Me')


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
	        grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 1, 2)
		
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









