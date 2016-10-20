# Extension-App Analyzer
# Part of Forensics Project
# BrowserHistoryAnalyzer )(Windows Specific)
# Author: Michael Schade

# Used to look at what Chrome apps and Chrome Extensions have been installed
# CHROME SPECIFIC

# Ext-App.txt is used as a small database for the program to pull
# from at this moment in development. Will be updated

import os


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
if (lst[i] == lst2[i]):
    print(lst3[i + 1] + " is installed")
    i += 1
else:
    print("not installed")
