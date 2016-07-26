# A GUI created to make installation of computers in a Fab Lab easier. 
# Fully tested on Ubuntu 14.04 64 bit.
#
# Features:
#    Install standard and neccessary applications for Ubuntu.

import os, sys, getpass, gtk

class fabinstaller():

    def __init__(self):
        user = getpass.getuser()
        print('Getting information for the GUI. Your User Name is: %s' % (user))
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Ultimate Fab Installer")
        self.window.set_default_size(500, 500)

        self.window.connect("delete_event", self.delete_event)

        self.box1 = gtk.HBox(False, 0)

        self.window.add(self.box1)
       
        self.close_button = gtk.Button("Close Button")
        self.close_button.connect("clicked", self.on_close_btn_clicked)

        self.box1.pack_start(self.close_button, True, True, 0)
       
        self.button2 = gtk.Button("Button 2")

        self.box1.pack_start(self.button2, True, True, 0)

        self.close_button.show()
        self.button2.show() 
        self.box1.show()
        self.window.show()


    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def on_close_btn_clicked(self, widget):
        gtk.main_quit()


def main():
   gtk.main()

if __name__ == "__main__":
   hello = fabinstaller()
   main()
