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
            self.cache = ("", None)

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

    def execQuery(self, query):
        if(self.cache[0] == query):
            return
        if self.db is None:
            self.connect_to_mysql()
        cursor = self.db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self.cache = (query, rows)

    def getRows(self):
        return self.cache[1]


#m = MySQL("192.168.99.100", 3306, "root", "", "mysql-development")
#m.execQuery("select * from student")
#rows = m.getRows()
#for row in rows:
#    print(row)
