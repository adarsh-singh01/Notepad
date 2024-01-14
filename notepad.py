from tkinter import *
import tkinter.messagebox as sandesha
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
root.geometry("800x800")
root.title("Untitled - Notepad")



def nf():
    global file
    root.title("Untitled - Notepad")
    file=None
    txtarea.delete(1.0,END)

def of():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        txtarea.delete(1.0,END)
        f=open(file,"r")
        txtarea.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Not_titled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(txtarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file +" - notepad"))
    else:
        f=open(file,"w")
        f.write(txtarea.get(1.0,END))
        f.close()

def cut():
    txtarea.event_generate(("<<Cut>>"))
def copy():
    txtarea.event_generate(("<<Copy>>"))
def paste():
    txtarea.event_generate(("<<Paste>>"))
def about():
    sandesha.showinfo("About Section","Notepad Replica by Adarsh")


txtarea=Text(root,font="lucida 15 ")
txtarea.pack(fill=BOTH,expand=True)

file=None

tabs=Menu(root)

m1=Menu(tabs,tearoff=0)
m2=Menu(tabs)


m1.add_command(label="New",command=nf)
m1.add_command(label="Open",command=of)
m1.add_command(label="Save",command=save)
m1.add_separator()
m1.add_command(label="Exit",command=quit)

m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)

tabs.add_cascade(label="File",menu=m1)
tabs.add_cascade(label="Edit",menu=m2)
tabs.add_cascade(label="About Us",command=about)

root.config(menu=tabs)

sbar = Scrollbar(txtarea)
sbar.pack(side="right", fill="y")
sbar.config(command=txtarea.yview)
txtarea.config(yscrollcommand=sbar.set)

root.mainloop()