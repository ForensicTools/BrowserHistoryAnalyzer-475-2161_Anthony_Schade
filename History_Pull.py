"""
Testing function; working on pulling browser history from local
file in default location to csv or readable file that can be parsed
through, text file.

Prereqs: Chrome must be installed in the default location.
         User must have admin right.

Schade_Anthony
"""

import os
import sqlite3


user_name = input("Enter the Username you wish to pull history for... ")

def history_grab():

    os.system("copy \"C:\\Users\\"+user_name+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History\" "
                                             "C:\\Users\\"+user_name+"\\AppData\\Local\\Temp")

    Link = sqlite3.connect("C:\\Users\\" + user_name + "\\AppData\\Local\\Temp\History")
    Zelda = Link.cursor()
    #Link.execute('SELECT * FROM History;')
    print(Zelda.rowcount)




    #date_string = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=timestamp)


history_grab()
