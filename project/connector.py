"""
Created on Wed Jan 22 2025

@Author: Elliot
"""


from  MySQLdb import _mysql, _exceptions

class Connector:
    def __init__(self):
        self.connection = None
        self.host = None
        self.user = None
        self.password = None
        self.database = None

    def test_connection(self, user, host, password):
        self.host = host
        self.user = user
        self.password = password

        try:
            self.connection = _mysql.connect(
                self.host, self.user, self.password
            )
        except _exceptions.Error as error:
            print(error)

    def get_databases(self):
        self.connection.query("SHOW DATABASES")
        r = self.connection.store_result()
        return [str(x[0])[1:].replace("'","") for x in r.fetch_row(maxrows=0)]

    def get_tables(self, database):
        self.database = database

        try:
            self.connection = _mysql.connect(
                self.host, self.user, self.password, self.database
            )
        except _exceptions.Error as error:
            print(error)

        self.connection.query("SHOW TABLES")
        r = self.connection.store_result()
        return [str(x[0])[1:].replace("'","") for x in r.fetch_row(maxrows=0)]