from database import Database

class DataService:
    def __init__(self, host, user, password, database):
        self.database = Database(host, user, password, database)

    def get_records(self):
        try:
            return self.database.fetch_records()
        except Exception as e:
            raise e