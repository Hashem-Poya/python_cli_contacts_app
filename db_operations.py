from db_connection import connection

class UserOperations:
    @staticmethod
    def insert(name, lastname, email, age, address, phone):
        db = connection()
        c = db.cursor()
        try:
            c.execute(
                '''
                    INSERT INTO user_info (name, lastname, email, age, address, phone)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (name, lastname, email, age, address, phone)
            )
        except Exception as e:
            print('Error occured...')
            print(e)
        db.commit()
    @staticmethod
    def get_info():
        db = connection()
        c = db.cursor()
        c.execute('SELECT * FROM user_info')
        rows = c.fetchall()
        db.commit()
        return rows

    @staticmethod
    def search(search_key):
        db = connection()
        c = db.cursor()
        print('Before DB execute method:', search_key)
        c.execute("SELECT * FROM user_info WHERE id LIKE ? OR name LIKE ? OR email LIKE ?;", (search_key, search_key, search_key))
        rows = c.fetchall()
        db.commit()
        return rows
    
    @staticmethod
    def update(name, lastname, email, age, address, phone):
        db = connection()
        c = db.cursor()
        print('USER EMAIL: ', email)
        sql = "UPDATE user_info set name = ?, lastname = ?, email = ?, age = ?, address = ?,phone = ? WHERE email LIKE ? ;"
        c.execute(sql, (name, lastname, email, age, address, phone, email))
        db.commit()
    
    @staticmethod
    def delete(delete_keyword):
        db = connection()
        c = db.cursor()
        sql = 'DELETE FROM user_info WHERE id LIKE ? OR name LIKE ? OR email LIKE ?;'
        c.execute(sql, (delete_keyword, delete_keyword, delete_keyword))
        db.commit()
    

