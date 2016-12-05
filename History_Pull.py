"""
Purpose: Copies the Chrome/Firefox History File from the default
location to the default temporary folder.
Function that will take in a username and a data type.
It will return the requested information to the user via the
sqlite3 plugin within python, based on
the information found in the History file.

Prereqs: Browsers must be installed in their default location.
         User must have admin rights.

Schade_Anthony_2016
"""

import os
import sqlite3

user_name = input("Enter the Username you wish to pull history for... ")
#data_retrieval_type = str(input("What type of data would you like to view? Type .help for a list of acceptable commands: ")).lower()


def history_Retrieval_Module():
    os.system("copy \"C:\\Users\\" + user_name + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History\" "
                                                 "C:\\Users\\" + user_name + "\\AppData\\Local\\Temp")
    default_file_path = str("C:\\Users\\" + user_name + "\\AppData\\Local\\Temp\History")

    status = True

    while status == True:

        data_retrieval_type = str(
            input("What type of data would you like to view or search for a website? \nType .help for a list of acceptable commands: ")).lower()
        try:
            Link = sqlite3.connect(default_file_path)
            e_cursor = Link.cursor()
            d_cursor = Link.cursor()
            c_cursor = Link.cursor()
            b_cursor = Link.cursor()
            a_cursor = Link.cursor()
        except:
            print('\n INVALID USERNAME ENTERED. User does not have History, or incorrect username')

        if data_retrieval_type == "downloads":
            Download_Ouput = open('Download_Output.txt', 'w', encoding='utf-8')
            Download_Ouput.write('Display format: (Time Downloaded), (Total File Size (Bytes)), (Downloaded Page Link), (Download Destination)\n')
            table_name_downloads = str('Downloads')
            column_name_downloads = str('Downloads')
            #a_cursor = Link.cursor()
            print("---------------------------------------------------")
            print("Display format: (Time Downloaded), (Total File Size (Bytes)), (Downloaded Page Link), (Download Destination)")
            for row in a_cursor.execute('SELECT datetime(((downloads.start_time/1000000)-11644473600), "unixepoch"), total_bytes,'
                                        ' referrer, target_path FROM downloads' .\
                                        format(table_name=table_name_downloads, column_name=column_name_downloads)):
                Download_Ouput.writelines("%s\n" % str(row))
                print(row)
            Download_Ouput.close()
            print("Display format: (Time Downloaded), (Total File Size (Bytes)), (Downloaded Page Link), (Download Destination)")
            print("---------------------------------------------------")

        elif data_retrieval_type == "url":
            url_output = open('URL_Output.txt', 'w', encoding='utf-8')
            url_output.write("Display format: (Time Visited), (Last Time Visited), (Website URL), (Website Title), (Number of Visits)")
            table_name_URL = str('URL')
            column_name_URL = str('URL')
            #b_cursor = Link.cursor()
            print("---------------------------------------------------")
            print("Display format: (Time Visited), (Last Time Visited), (Website URL), (Website Title), (Number of Visits)")
            for row in b_cursor.execute('SELECT datetime(((V.visit_time/1000000)-11644473600), "unixepoch"),'
                                        ' datetime(((U.last_visit_time/1000000)-11644473600), "unixepoch"),U.url, U.title, '
                                        'U.visit_count FROM urls AS U, visits AS V WHERE U.id = V.url'.\
                                                format(tn=table_name_URL, cn=column_name_URL)):
                url_output.writelines("%s\n" % str(row))
                print(row)
            url_output.close()
            print("Display format: (Time Visited), (Last Time Visited), (Website URL), (Website Title), (Number of Visits)")
            print("---------------------------------------------------")

        elif data_retrieval_type == ".help":
            print('\n List of commands: \n'
                  ' Website URLs: URL \n'
                  ' Recent Searches: Searches \n'
                  ' Search a Term: Search Term \n'
                  ' List Downloaded Content: Downloads \n'
                  ' Repeat This List: .help \n')

        elif data_retrieval_type == "searches":
            searches_output = open('Searches_output.txt', 'w', encoding='utf-8')
            searches_output.write("Display format: Search Term")
            table_name_search = str('Searches')
            column_name_search = str('Searches')
            #c.cursor = Link.cursor()
            print("---------------------------------------------------")
            print("Display format: Search Term")
            for row in c_cursor.execute('Select lower_term from keyword_search_terms'.\
                                       format(tn=table_name_search, cn=column_name_search)):
                searches_output.writelines('%s\n' % str(row))
                print(row)
            print("Display format: Search Term")
            print("---------------------------------------------------")

        elif data_retrieval_type == "search term":
            search_term_output = open('Search_Term_Output', 'w', encoding='utf-8')
            table_name_search_term = str('search term')
            column_name_search_term = str('search term')
            #d.cursor = Link.cursor()
            term = str(
                input("What Website would you like to search for? (ex. google, facebook): ")).lower()
            print("---------------------------------------------------")
            for row in d_cursor.execute('select url from urls where url like "%'+term+'%"'.\
                                        format(tn=table_name_search_term, cn=column_name_search_term)):
                search_term_output.writelines('%s\n' % str(row))
                print(row)

            for row in d_cursor.execute('select COUNT(url) from urls where url like "%'+term+'%"'):
                print(term +' Has been accessed ' + str(row) + ' times since the creation of the History log:')

        elif data_retrieval_type == "visual":
            visual_output = open('visual.csv', 'w', encoding='utf-8')
            table_name_visual = str('Visual')
            column_name_visual = str('Visual')
            for row in e_cursor.execute('select url, visit_count from urls'.\
                                        format(tn=table_name_visual, cn=column_name_visual)):
                visual_output.write(str('id, value'))
                visual_output.write(str(row))
            visual_output.close()
            print("Finished")

        else:
            print('\n INVALID DATA TYPE')
            print('\n List of commands: \n'
                  ' Website URLs: URL \n'
                  ' List Downloaded Content: Downloads \n'
                  ' View Recent Searches: Searches \n'
                  ' Repeat This List: .help')


        choice = input("Type 'Go' to begin again or type 'quit': ")
        if choice == 'go':
            pass
        elif choice == 'quit':
            print("Goodbye")
            status = False
            exit()

history_Retrieval_Module()

