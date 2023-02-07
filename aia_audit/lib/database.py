import sqlite3

class Database:

    db_file = "aia_audit/data/database.db"
    conn = None
    cursor = None

    def __init__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def check_database(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        if not self.cursor.fetchall():
            self.create_tables()

    def create_tables(self):
        self.create_table("scan_types", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT")
        self.create_table("scan_types_modules", "id INTEGER PRIMARY KEY AUTOINCREMENT, scan_type INTEGER, module INTEGER, FOREIGN KEY(scan_type) REFERENCES scan_types(id), FOREIGN KEY(module) REFERENCES modules(id)")
        self.create_table("module_types", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT")
        self.create_table("modules", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, type INTEGER, FOREIGN KEY(type) REFERENCES module_types(id)")
        self.create_table("scans", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, status TEXT, type TEXT, target TEXT")
        self.create_table("settings", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, value TEXT")

    def populate_tables(self):
        self.insert("scan_types", "name", "'Simple'")
        self.insert("scan_types", "name", "'Complete'")
        self.insert("scan_types", "name", "'Custom'")

        self.insert("module_types", "name", "'Information Gathering'")
        self.insert("module_types", "name", "'Vulnerability Scanning'")
        self.insert("module_types", "name", "'Exploitation'")
        self.insert("module_types", "name", "'Post Exploitation'")
        self.insert("module_types", "name", "'Reporting'")
        self.insert("module_types", "name", "'Other'")

        self.insert("modules", "name, description, type", "'Nmap', 'Nmap is a free and open source utility for network discovery and security auditing. Many systems and network administrators also find it useful for tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime.', 1")


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

    def query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def query_select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()