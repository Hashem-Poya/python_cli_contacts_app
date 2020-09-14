import sqlite3
from sqlite3 import Error
import os
import utlis


def connection():
    conn = None
    try:

        db_path = utlis.create_dir_if_not_exists('Database_dir')        
        conn = sqlite3.connect(db_path + '/' + 'Contacts.db')
    

        c = conn.cursor()

        c.execute('''
                CREATE TABLE IF NOT EXISTS user_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                email TEXT NOT NULL,
                age INT NOT NULL,
                address TEXT NOT NULL,
                phone TEXT NOT NULL
            );

        ''')
        


        conn.commit()
        
    except sqlite3.Error as e:
        print(e)
    finally:
        os.chdir('../')

    return conn

