from Tkinter import *
from PIL import Image, ImageTk
import os
import string
from pprint import pprint
#from ctypes import windll



class TileItem(Frame):
    def __init__(self, master=None):
        
        self.Obj = master
        #self,index,f,m1
        w = Button(self.Obj[3], compound="left",fore='#1d1d1d',borderwidth=0,padx = 10, text=self.Obj[2],command=lambda:self.Obj[0].dir_callback(self.Obj[2]))
        w.grid(row=self.Obj[1],column=1,pady=2,sticky='we')
        w.configure(image=self.Obj[0].img_folder,bg= '#ffffff',width="300",height="20")
        
        w.bind( "<Button-3>", self.popUpMenu )

    def popUpMenu( self, event ):
        self.Obj[0].menu = Menu( self.Obj[0].parent, tearoff = 0 )
        colors = [ "White", "Blue", "Yellow", "Red", "Pink", "Gray", "Purple"]
        for item in colors:
            self.Obj[0].menu.add_radiobutton(label = self.Obj[2])
        self.Obj[0].menu.post( event.x_root, event.y_root )