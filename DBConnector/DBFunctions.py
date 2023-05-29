import pyodbc

class DBConnector:
    def __init__(self, server, database, driver='{ODBC Driver 17 for SQL Server}'):
        self.server = server
        self.database = database
        self.driver = driver
        self.conn = None
        self.cursor = None


    def connect(self):
        connection_string = 'DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';Trusted_Connection=yes;'
        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()


    def disconnect(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

    
    def execute_query(self, sql, values=None):
        self.cursor.execute(sql, values) if values else self.cursor.execute(sql)
        self.conn.commit()
    

    def execute_read_query(self, sql, values=None):
        self.cursor.execute(sql, values) if values else self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows 


connector = DBConnector(server='DESKTOP-REV4M37', database='BLING_System')

connector.connect()

# # Example of executing an INSERT query
# sql = "INSERT INTO YourTableName (column1, column2) VALUES (?, ?)"
# values = ('value1', 'value2')
# connector.execute_query(sql, values) 

# # Example of executing a SELECT query
# sql = "SELECT * FROM YourTableName"
# result = connector.execute_read_query(sql)
# for row in result:
#         print(row) 

# connector.disconnect() 