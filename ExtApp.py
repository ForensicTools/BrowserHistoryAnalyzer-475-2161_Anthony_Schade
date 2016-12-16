##Extension-App Analyzer
##Part of Forensics Project
import os
from tkinter import *
from tkinter import messagebox


def base():
    file = open('Ext-App.txt')
    lst= []
    for line in file:
        temp = line.split(',')
        lst.append(temp[0])
    messagebox.showinfo(lst)

top = Tk()
top.geometry("100x100")
text = Text(top)
text.insert(INSERT, "hi")

#B1 = Button(top, text = "Hello")
#B1.place(x=35,y=50)

top.mainloop()