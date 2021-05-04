# connect the mariaDB dictionary database
# Module Imports
import mariadb
import sys

class Maria(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        if (self.conn == None or self.cur == None):
            # Connect to MariaDB Platform
            try:
                self.conn = mariadb.connect(
                    user="root",
                    password="whatever",
                    host="127.0.0.1",
                    port=3306,
                    database="entries"
                )
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
                sys.exit(1)
            # Get Cursor
            self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def execute(self, sql, param = False):
        self.connect()
        try:
            if (param != False):
                result = self.cur.execute(sql, param)
            else:
                result = self.cur.execute(sql)
            # default auto-commit
            return result
        except mariadb.Error as e:
            print(f"Error: {e}")
