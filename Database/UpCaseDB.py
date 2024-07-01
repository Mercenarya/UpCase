import sqlite3
import os

current_path = os.path.dirname(os.path.abspath(__file__))
DB_path = os.path.join(current_path,"upcase.db")
DB = sqlite3.connect(DB_path,check_same_thread=False)
cursor = DB.cursor()



def Profile():
    Setprofile = '''
        CREATE TABLE profile (
            id INT PRIMARY KEY,
            image VARCHAR(500),
            name VARCHAR(50),
            profession VARCHAR(50),
            company VARCHAR(50),
            status VARCHAR(50),
            birth DATETIME,
            note VARCHAR(500)
        )
    '''
    return Setprofile

def Drop():
    dropCmd = '''ALTER TABLE profile DROP COLUMN note'''
    return dropCmd

def PragmaList():
    Pragma = '''PRAGMA table_list'''
    return Pragma
try:
    if sqlite3.Connection:
        print("Connection set up")
        print("Release list of table")
        DB.execute(Drop())
        print("Command in process")
        

        DB.commit()
    elif sqlite3.Error:
        print("DB Error")
except sqlite3.Error as error:
    print(error)
         



