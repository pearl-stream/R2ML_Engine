##https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
import mysql.connector


class MySQL():
    cache = {}

    def __init__(self, host, port, username, password, database):
            self.host = host
            self.port = port
            self.username = username
            self.password = password
            self.database = database
            self.db =""

    def connect_to_mysql(self):
        try:
            self.db = mysql.connector.connect(host=self.host,user = self.username ,password = self.password, database = database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def execQuery(self, query) :
        if self.db is None:
            connect_to_mysql()
        cursor = self.db.cursor()
        cursor.execute(query)


m = MySQL("127.0.0.1", 3306, "root", "", "mysql-development")
m.execQuery()
