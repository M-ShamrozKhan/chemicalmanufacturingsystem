from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Chemical Manufacturing System")
        self.root.config(bg="white")
        self.root.focus_force()
       #============title================
        lbl_title=Label(self.root,text="View Customer Bill ",font=("goudy old style",30),bg="#184a45",fg="white",bd=5,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        
        
        
        
if __name__=="__main__":         
    root=Tk() 
    obj=salesClass(root)
    root.mainloop()