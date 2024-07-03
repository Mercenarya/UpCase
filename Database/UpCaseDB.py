import sqlite3
import os

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
def List():
    SetList = '''
        SELECT * FROM Profile
    '''
    return SetList

def Drop():
    dropCmd = '''ALTER TABLE profile DROP COLUMN note'''
    return dropCmd

def PragmaList():
    Pragma = '''PRAGMA table_list'''
    return Pragma
try:
    if sqlite3.Connection:
        print("Connection set up")
        cursor.execute(List())
        print("Release list of table")
        for obj in cursor.fetchall():
            print(obj)
        print("Command in process")

        DB.commit()
    elif sqlite3.Error:
        print("DB Error")
except sqlite3.Error as error:
    print(error)
         



