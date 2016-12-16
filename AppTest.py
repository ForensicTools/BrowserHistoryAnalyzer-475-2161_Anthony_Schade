# Extension-App Analyzer
# Part of Forensics Project
# BrowserHistoryAnalyzer (Windows Specific)
# Schade_Anthony_2016

# Used to look at what Chrome apps and Chrome Extensions have been installed
# CHROME SPECIFIC

# Ext-App.txt is used as a small database for the program to pull
# from at this moment in development. Will be updated

import os
from tkinter import *
import re

def go():
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

    lst4= []

    for s in lst:
        for item in lst2:
            if item in s:
                print(lst3[i] + " is installed")
                i += 1
            #print(lst4[i])

    appoutput = open('appsOutput.txt', 'w')
    for line in lst3:
        appoutput.write(line + "\n")

#
#Working on getting bookmarks
#
def books():
    bookpath = os.path.join("C:\\", "Users", "%username%" ,"AppData","Local","Google","Chrome","User Data","Default")
    bookpath2 = str("\"%s\"" %bookpath)
    bookpath3 = os.path.join("C:\\", "Users", "%username%" ,"AppData","Local","Google","Chrome","User Data","Default","Bookmarks")
    path3 = str("\"%s\"" %bookpath3)


##Get contents of Bookmarks file and output to text
##file in the directory of THIS program
    os.system("type " + path3 + " > bookmarks.txt" )


##Take Bookmarks file and add contents to a list
##
    marks = open('bookmarks.txt')
    lst5 = []
    point = 'h'


    for line in marks:
    #line = re.sub('"url": "', '', line)
        line = line.strip('} {"url": "')
        re.sub('}  {', '',line)
        if "http" in line:
            lst5.append(line)



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
    text.insert(INSERT, lst5)
    text.pack()
    root.wm_title("Bookmark Visualizer")

    root.iconbitmap("bookmarks-icon-24532-16x16.ico")
    root.mainloop()

    userBookmarks = open("userBookmarks.txt", 'w')

    for line in lst5:
        userBookmarks.write(line)

#B1 = Button(root, text = "Hello", command = close())
#B1.place(x=35,y=50)

    def close():
        root.destroy()

