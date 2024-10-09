import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def fetch_records(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `db 2`")  # Use backticks for table names with spaces
            records = cursor.fetchall()
            return records
        except mysql.connector.Error as err:
            raise Exception(f"Database Error: {str(err)}")
        finally:
            cursor.close()
            conn.close()