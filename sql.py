import mysql.connector
from mysql.connector import Error
from decouple import config
host = config('HOST')
user = config('USER')
password = config('PASSWORD')


class Connection:
    def __init__(self):
        self.conn = mysql.connector.connect(host, user, password)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXIST 
        """)