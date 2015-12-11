# A GUI created to make installation of computers in a Fab Lab easier. 
# Fully tested on Ubuntu 14.04 64 bit.
#
# Features:
#    Install standard and neccessary applications for Ubuntu.

import os, sys, getpass, gtk

class fabinstaller(gtk.Window):

    def __init__(self):
        user = getpass.getuser()
        print('Getting information for the GUI. Your User Name is: %s' % (user))
        gtk.Window.__init__(self)
        self.button()

    def button(self):
        install_btn = gtk.Button("Install")
        close_btn = gtk.Button("Close")

        install_btn.set_size_request(100, 40)
        install_btn.connect("clicked", self.on_button_clicked)
        close_btn.connect("clicked", self.on_close_btn_clicked)
        
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 5)
        
        valign = gtk.Alignment(1, 0, 0, 0)
        vbox.pack_start(valign)
        halign = gtk.Alignment(1, 0, 0, 0)
        
        hbox.add(install_btn)
        hbox.add(close_btn)
        
        halign.add(hbox)
        
        vbox.pack_start(halign, False, False, 5)

        self.add(vbox)

    def on_button_clicked(self, widget):
        print("Hello World")

    def on_close_btn_clicked(self, widget):
        print("Closing The Application")
        sys.exit(1)

app=fabinstaller()
app.connect("delete-event", gtk.main_quit)
app.set_default_size(500, 500)
app.set_title("Ultimate Fab Installer")
app.show_all()
gtk.main()
