import sqlite3
import os
import datetime

current_path = os.path.dirname(os.path.abspath(__file__))
DB_path = os.path.join(current_path,"upcase.db")
DB = sqlite3.connect(DB_path,check_same_thread=False)
cursor = DB.cursor()



def Profile():
    Setprofile = '''
        CREATE TABLE Profile (
            id INT PRIMARY KEY,
            image VARCHAR(500),
            name VARCHAR(500),
            profession VARCHAR(500),
            company VARCHAR(500),
            status VARCHAR(500),
            birth DATETIME
            
        )
    '''
    return Setprofile
Date_str = '2004-10-17'
Converted_date = datetime.datetime.strptime(Date_str, '%Y-%m-%d')
Release_date = Converted_date.strftime('%Y-%m-%d')


def Insert():
    Setcmd = '''UPDATE Profile set birth = ? WHERE id = 1'''
    return Setcmd
def List():
    SetList = '''
        SELECT * FROM Profile
    '''
    return SetList

def Drop():
    dropCmd = '''ALTER TABLE profile DROP COLUMN birth'''
    return dropCmd
def NewCOl():
    dropCmd = '''ALTER TABLE profile ADD COLUMN birth VARCHAR(500)'''
    return dropCmd
def PragmaList():
    Pragma = '''PRAGMA table_list'''
    return Pragma
try:
    if sqlite3.Connection:
        print("Connection set up")
        cursor.execute(NewCOl())
        # print("Release list of table")
        # for obj in cursor.fetchall():
        #     print(obj)
        print("Command in process")


        DB.commit()
    elif sqlite3.Error:
        print("DB Error")
except sqlite3.Error as error:
    print(error)
         



