from tkinter import *
from PIL import Image, ImageTk
import os
import string
from ctypes import windll

class m_r():
    name=None
    img=None
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.initUI()
    def menutools(self):
        
        m1 = PanedWindow(self.parent)
       	m1.grid(row=0,column=0)
        
        self.img_back = ImageTk.PhotoImage(Image.open('Arrow Left 04-WF.png'))
        self.img_back_2 = ImageTk.PhotoImage(Image.open('Arrow Right 04-WF.png'))

        w = Button(m1, compound="top",fore='#ffffff',borderwidth=0,padx = 10)
            #w = Label(self.parent,image=self.img_folder)
        w.grid(row=0,column=0)
        w.configure(image=self.img_back,width="50",height="48")

        w = Button(m1, compound="top",fore='#ffffff',borderwidth=0,padx = 10)
            #w = Label(self.parent,image=self.img_folder)
        w.grid(row=0,column=1)
        w.configure(image=self.img_back_2,width="50",height="48")
            #w.pack(side=LEFT)
    def menu_rich(self):
        self.dat=[m_r(),m_r(),m_r(),m_r()]
        
        self.dev = ImageTk.PhotoImage(Image.open('Disk-HDD.png'))

        self.dat[0].name='Usuario'
        self.dat[0].img=ImageTk.PhotoImage(Image.open('Usuario.png'))

        self.dat[1].name='Documentos'
        self.dat[1].img=ImageTk.PhotoImage(Image.open('Documentos.png'))

        self.dat[2].name='Imagenes'
        self.dat[2].img=ImageTk.PhotoImage(Image.open('Imagenes.png'))

        self.dat[3].name='Descargas'
        self.dat[3].img=ImageTk.PhotoImage(Image.open('Cloud-Download.png'))
        index=1

        for i,f in enumerate(self.dat):
            
            w = Button(self.parent, compound="top",fore='#ffffff',borderwidth=0,padx = 10, text=f.name)
            #w = Label(self.parent,image=self.img_folder)
            w.grid(row=index,column=0,padx=2, pady=2)
            w.configure(image=f.img,bg= '#7e3878',width="86",height="70")
            #w.pack(side=LEFT)
            index=(1+index)


        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]:
            
            w = Button(self.parent, compound="top",fore='#ffffff',borderwidth=0,padx = 10, text=letter)
            w.grid(row=index,column=0,padx=2, pady=2)
            w.configure(image=self.dev,bg= '#7e3878',width="86",height="70")
            


    def initUI(self):
        
        self.menutools()
        self.menu_rich()
        self.img_folder = ImageTk.PhotoImage(Image.open('Folder-New-01-48.png'))
        #index=1
        #for f in self.get_filepaths("C:\\Users\\jmart\\Documents\\git\\Gorpy_Exprorer"):

        #    w = Button(self.parent, compound="top",fore='#ffffff',borderwidth=0,padx = 10, text=f)
        #    #w = Label(self.parent,image=self.img_folder)
        #    w.grid(row=index,column=0,padx=2, pady=2)
        #    w.configure(image=self.img_folder,bg= '#7e3878',width="86",height="100")
            #w.pack(side=LEFT)
        #    index=(1+index)

    def get_filepaths(self,directory):
        
        file_paths = []  # List which will store all of the full filepaths.

        # Walk the tree.
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = filename
                file_paths.append(filepath)  # Add it to the list.

        return file_paths  # Self-explanatory.


def main():
    root = Tk()
    app = Application(root)
    app.parent.geometry('300x200+100+100')
    app.parent.configure(background = 'white')
    app.mainloop()

main()