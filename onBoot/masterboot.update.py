from datetime import datetime
from tkinter import messagebox as m
from tkinter import Tk

print("functional")
version = 0.0
strVersion = "0.0"
def toBoot():
    date = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    boot = open("record\\boot.ini", "a")
    boot.write("\n")
    boot.write("[version[" + strVersion + "]][date["+ date +"]]")
    boot.write("\n")
    boot.close()
def  if_prerealese():
    if version < 3:
        root=Tk()
        m.showinfo("note", "Nytron Music is in a prerealese version. ("+ strVersion +") \n please dont mind certant features not being included. \n Thanks! (: ")
        root.destroy()
