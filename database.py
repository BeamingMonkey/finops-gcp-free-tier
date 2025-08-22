import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS usage(
                service TEXT,
                usage REAL,
                unit TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS risks(
                service TEXT,
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save_usage(self, data):
        c = self.conn.cursor()
        for d in data:
            c.execute("INSERT INTO usage(service, usage, unit) VALUES (?, ?, ?)", 
                      (d["service"], d["usage"], d["unit"]))
        self.conn.commit()

    def save_risks(self, risks):
        c = self.conn.cursor()
        for r in risks:
            c.execute("INSERT INTO risks(service, message) VALUES (?, ?)", 
                      (r["service"], r["message"]))
        self.conn.commit()
