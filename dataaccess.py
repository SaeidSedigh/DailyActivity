import sqlite3

DataModel = "M_Base"

class DataAccess:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
    #Create new record in database
    def create_database(self, sql_code):
        with open(sql_code, 'r') as file:
            sql_script = file.read()
        self.cursor.executescript(sql_script)
        self.connection.commit()

    def CommitWithParameter(self, Query, params : tuple):
        try:
            self.cursor.execute(Query, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error executing query: {e}")
            return False
        
    def Insert(self , Query , DataModel):
        placeholders = ', '.join(['?'] * len(DataModel.ColumnList))
        Query = f"INSERT INTO {DataModel.TableName} ({DataModel.Columns()}) VALUES ({placeholders})"
        self.CommitWithParameter(Query , DataModel.Values())
        last_row_id = self.cursor.lastrowid
        DataModel.Id = last_row_id
        return DataModel

    def GetOneRecord(self, query: str, params: tuple):
        self.cursor.execute(query, params)
        record = self.cursor.fetchone()
        if record:
            return record
        return None

    # Implement update and delete methods as needed

# Usage example
db = DataAccess('example.db')
db.create_database('create_tables.sql')
