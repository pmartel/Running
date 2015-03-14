#!/usr/bin/env python 
""" this comes from tkinter.pdf  It runs in IDLE, but gives errror messages
when run from the command line """
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
