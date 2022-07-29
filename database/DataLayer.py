
import mysql.connector
import os

#should be passed in constructor if component needs data from backend
class DataLayer:
    def __init__(self):
        
        self.start_connection_and_cursor()
        
        try:
            #initialize purchasepeer_db
            self.cursor.execute("""CREATE DATABASE IF NOT EXISTS purchasepeer_db""")

            #creates transaction table
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
                id INT(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                date DATE,
                category VARCHAR(255),
                amount DOUBLE(12,2) NOT NULL,
                description VARCHAR(255),
                type VARCHAR(255) NOT NULL
                )""")
            self.conn.commit()
        except:
            self.conn.rollback()
            raise Exception("Could not access necessary database")
        
        self.conn.close()
        
    def start_connection_and_cursor(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = os.environ.get("DB_USER"),
            passwd = os.environ.get("DB_PASS"),
            database = "purchasepeer_db"
            )
        self.cursor = self.conn.cursor()
    
    def execute(self, command, values):
        try:
            self.start_connection_and_cursor()
            self.cursor.execute(command,values)
            self.conn.commit()
        except:
            self.conn.rollback()
            raise Exception("Command was invalid")
        self.conn.close()
        
        
    #for debugging purposes only    
    def show_all_rows(self):
        # execute your query
        self.cursor.execute("SELECT * FROM transactions")
        
        # fetch all the matching rows 
        result = self.cursor.fetchall()
        
        # loop through the rows
        for row in result:
            print(row)