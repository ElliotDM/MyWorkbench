import mysql.connector

class Connector:
    def __init__(self):
        self.connection = None
        self.host = None
        self.username = None
        self.password = None
        self.database = None

    def connect_to_db(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password
            )
        except mysql.connector.Error as error:
            return error