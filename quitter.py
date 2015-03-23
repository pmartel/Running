#!/usr/bin/env python 
""" this comes from tkinter.pdf  It runs in IDLE, but gives errror messages
when run from the command line """
''' if the environmant variable PYTHONCASEOK is set, this will run from the
command line.  The problem was that sys.path was
['', 'C:\\Windows\\system32\\python34.zip', 'C:\\Python34\\DLLs',
 'C:\\Python34\\lib', 'C:\\Python34', 'C:\\Python34\\lib\\site-packages']
 and that the lib directory is C:\Python34\Lib (with a "L")
'''
from tkinter import *

class Application(Frame): 
    def __init__(self, master=None):
        Frame.__init__(self, master) 
        self.grid() 
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = Button(self, text='Quit', command=self.quit) 
        self.quitButton.grid()
        
app = Application() 
app.master.title('Sample application')
app.mainloop()
