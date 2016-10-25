"""
Purpose: Function that will take in a username and a data type.
It will return the requested information to the user based on
the information found in the Chrome History file.

Prereqs: Chrome must be installed in the default location.
         User must have admin rights.

Schade_Anthony
"""

import os
import sqlite3

user_name = input("Enter the Username you wish to pull history for... ")
data_retrieval_type = str(input("What type of data would you like to view? Type .help for a list of acceptable commands: "))


def history_Retrieval_Module():
    os.system("copy \"C:\\Users\\" + user_name + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History\" "
                                                 "C:\\Users\\" + user_name + "\\AppData\\Local\\Temp")
    default_file_path = str("C:\\Users\\" + user_name + "\\AppData\\Local\\Temp\History")
    try:
        Link = sqlite3.connect(default_file_path)
    except:
        print('\n INVALID USERNAME ENTERED. User does not have History, or incorrect username')

    if data_retrieval_type == "Downloads":
        table_name_downloads = str('Downloads')
        column_name_downloads = str('Downloads')
        a_cursor = Link.cursor()
        print("---------------------------------------------------")
        print("Display format: (Time Downloaded), (Total File Size (Bytes)), (Downloaded Page Link), (Download Destination)")
        for row in a_cursor.execute('SELECT datetime(((downloads.start_time/1000000)-11644473600), "unixepoch"), total_bytes,'
                                    ' referrer, target_path FROM downloads' .\
                                    format(table_name=table_name_downloads, column_name=column_name_downloads)):
            print(row)
        print("---------------------------------------------------")

    elif data_retrieval_type == "URL":
        table_name_URL = str('URL')
        column_name_URL = str('URL')
        b_cursor = Link.cursor()
        print("---------------------------------------------------")
        for row in b_cursor.execute('SELECT datetime(((V.visit_time/1000000)-11644473600), "unixepoch"),'
                                    ' U.url, U.title FROM urls AS U, visits AS V WHERE U.id = V.url;'.\
                    format(tn=table_name_URL, cn=column_name_URL)):
            print(row)
        print("---------------------------------------------------")

    else:
        print('\n INVALID DATA TYPE')
        print('\n List of commands: \n'
              ' Website URLs: URL \n'
              ' List Downloaded Content: Downloads')

history_Retrieval_Module()

