import mysql.connector


class UseDataBase:
    def __init__(self, dbconfig: dict) -> None:
        self.dbconfig = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
