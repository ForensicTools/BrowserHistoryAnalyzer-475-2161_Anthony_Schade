# Extension-App Analyzer
# Part of Forensics Project
# BrowserHistoryAnalyzer )(Windows Specific)
# Author: Michael Schade

# Used to look at what Chrome apps and Chrome Extensions have been installed
# CHROME SPECIFIC

# Ext-App.txt is used as a small database for the program to pull
# from at this moment in development. Will be updated

import os
from tkinter import *


file = open('Ext-App.txt')

lst3 = []
lst= []
for line in file:
    temp = line.split(',')
    lst.append(temp[0])
    vari = temp[1]
    vari2 = vari.strip("\n")
    lst3.append(vari2)



path = os.path.join("C:\\", "Users", "%username%" ,"AppData","Local","Google","Chrome","User Data","Default","Extensions")
path2 = str("\"%s\"" %path)
os.system("dir /b " + path2 + " > installed.txt")


installed = open('installed.txt')


lst2 = []
for line in installed:
    line.split(',')
    var = line.strip("\n")
    lst2.append(var)

i = 0

for s in lst:
    for item in lst2:
        if item in s:
            print(lst3[i] + " is installed")
            i += 1

#
#Working on getting bookmarks
#

bookpath = os.path.join("C:\\", "Users", "%username%" ,"AppData","Local","Google","Chrome","User Data","Default")
bookpath2 = str("\"%s\"" %bookpath)
bookpath3 = os.path.join("C:\\", "Users", "%username%" ,"AppData","Local","Google","Chrome","User Data","Default","")
os.system("cd " + bookpath3 + " Bookmarks > bookmarks.txt")



#for line in marks:
 #   if "http" in line:
  #      lst5.append(line)
#for line in lst5:
#    print(line)


##
##
##
##
##
##Adding support for visualization
##Using for visual representation of bookmarks
##
##
##
def onclick():
   pass
def close():
    root.destroy()

root = Tk()
text = Text(root)
text.insert(INSERT, *lst2)
text.pack()
root.wm_title("Bookmark Visualizer")

root.mainloop()

B1 = Button(root, text = "Hello", command = close())
B1.place(x=35,y=50)

def close():
    root.destroy()