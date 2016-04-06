from Tkinter import *
from PIL import Image, ImageTk
import os


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.initUI()

    def initUI(self):
        

        self.img_folder = ImageTk.PhotoImage(Image.open('Folder-New-01-48.png'))
        index=0
        for f in self.get_filepaths("/home/jmartell/Documentos/git/Gorpy_Exprorer"):
            Label(self.parent,text=f,justify=RIGHT,bg= '#ffffff').grid(row=index,column=1)

            w = Label(self.parent,image=self.img_folder)
            w.grid(row=index,column=0)
            w.configure(image=self.img_folder,bg= '#ffffff')
            #w.pack(side=TOP, fill=BOTH, expand=YES)
            index=(1+index)

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