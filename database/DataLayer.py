
import sqlite3

# should be used  if component needs data from backend
class DataLayer:
    def __init__(self):

        self.start_connection_and_cursor()

        try:
            # creates transaction table
            self.cursor.execute("""CREATE TABLE if not exists transactions(
                id INTEGER PRIMARY KEY,
                date text,
                category text,
                amount real NOT NULL,
                description text,
                type text NOT NULL
                )""")
            self.conn.commit()
        except BaseException as exception:
            self.conn.rollback()
            print(exception)
            raise Exception("Could not access necessary database")

        self.conn.close()

    def start_connection_and_cursor(self):
        self.conn = sqlite3.connect("purchasepeer.db")
        self.cursor = self.conn.cursor()

    def execute(self, command, values):
        try:
            self.start_connection_and_cursor()
            self.cursor.execute(command, values)
            self.conn.commit()
        except:
            self.conn.rollback()
            raise Exception("Command was invalid")
        
        
        
        self.show_all_rows()
        self.conn.close()

    # for debugging purposes only
    def show_all_rows(self):
        self.start_connection_and_cursor()
        # execute your query
        self.cursor.execute("SELECT * FROM transactions")

        # fetch all the matching rows
        result = self.cursor.fetchall()

        # loop through the rows
        for row in result:
            print(row)
