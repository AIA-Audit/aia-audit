import sqlite3

class Database:

    db_file = None
    conn = None
    cursor = None

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, columns))
        self.conn.commit()

    def insert(self, table_name, columns, values):
        self.cursor.execute("INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, values))
        self.conn.commit()


    def select(self, table_name, columns, where=None):
        if where:
            self.cursor.execute("SELECT {} FROM {} WHERE {}".format(columns, table_name, where))
        else:
            self.cursor.execute("SELECT {} FROM {}".format(columns, table_name))
        return self.cursor.fetchall()

    def update(self, table_name, set, where):
        self.cursor.execute("UPDATE {} SET {} WHERE {}".format(table_name, set, where))
        self.conn.commit()

    def delete(self, table_name, where):
        self.cursor.execute("DELETE FROM {} WHERE {}".format(table_name, where))
        self.conn.commit()

    def close(self):
        self.conn.close()
