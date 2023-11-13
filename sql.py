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
        self.create_database()
        self.create_tables()

    def create_database(self):
        self.cursor.execute("""
        CREATE DATABASE IF NOT EXISTS todolist;
        """)

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE `todolist`.`items` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `itemname` VARCHAR(45) NULL,
        `dateadded` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
        `currentstatus` TINYINT DEFAULT 1,
        `archived` TINYINT DEFAULT 0,
        PRIMARY KEY (`id`));
        """)

    def insert_entry(self, desc):
        self.cursor.execute(f"""
        INSERT INTO `todolist`.`items`(itemname) VALUES ('{desc}')
        """)
