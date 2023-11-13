import mysql.connector
from mysql.connector import Error
from decouple import config
host = config('HOST')
user = config('USER')
password = config('PASSWORD')


class Connection:
    def __init__(self):
        self.conn = mysql.connector.connect(host=host, user=user, password=password)
        self.cursor = self.conn.cursor()
        self.create_database()
        self.create_table()

    def create_database(self):
        self.cursor.execute("""
        CREATE DATABASE IF NOT EXISTS todolist;
        """)

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS `todolist`.`items` (
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
        self.conn.commit()

    def retrieve_non_archived(self):
        self.cursor.execute("""
        SELECT * FROM `todolist`.`items` WHERE archived = 0;
        """)

    def retrieve_all(self):
        self.cursor.execute("""
        SELECT * FROM `todolist`.`items`;
        """)

    def update_archive_status(self, entryid):
        self.cursor.execute(f"""
        UPDATE `todolist`.`items`
        SET archived = NOT archived
        WHERE id = {entryid}
        """)
        self.conn.commit()

    def edit_entry(self, entryid, entrytext):
        self.cursor.execute(f"""
        UPDATE `todolist`.`items`
        SET itemname = {entrytext}
        WHERE id = {entryid}
        """)
        self.conn.commit()

