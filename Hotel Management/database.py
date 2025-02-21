import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            self.cursor = self.conn.cursor()
            print(" Database Connected Successfully!")
        except mysql.connector.Error as err:
            print("Database Connection Failed:",err)

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values or ())
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Error:",err)

    def fetch_data(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
