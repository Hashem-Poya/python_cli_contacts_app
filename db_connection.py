import sqlite3
from sqlite3 import Error

def connection():
    conn = None
    try:
        conn = sqlite3.connect('Contacts.db')
        backup = sqlite3.connect('backup.db')
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
        conn.backup(backup)
        backup.close()
    except sqlite3.Error as e:
        print(e)
    return conn

