##https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
import mysql.connector


class MySQL():


    def __init__(self, host, port, username, password, database):
            self.host = host
            self.port = port
            self.username = username
            self.password = password
            self.database = database
            self.db = None
            self.cache = ("", None, None)

    def connect_to_mysql(self):
        print("Trying to connect to db")
        try:
            self.db =  mysql.connector.connect(host=self.host,user = self.username ,password = self.password, database = self.database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def translateRowsToKeyValue(self, cursor):
        field_to_index_map = {cursor.description[i][0] : i for i in range(len(cursor.description))}
        return field_to_index_map

    def execQuery(self, query):
        if(self.cache[0] == query):
            return
        if self.db is None:
            self.connect_to_mysql()
        cursor = self.db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        field_to_index_map = self.translateRowsToKeyValue(cursor)
        self.cache = (query, rows, field_to_index_map)

    def getRows(self):
        return self.cache[1]
    def getColumnNameToKey(self):
        return self.cache[2]
