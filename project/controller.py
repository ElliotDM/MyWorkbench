"""
Created on Tue Jan 21 2025

@Author: Elliot
"""


from login_dialog import Login
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt

class Controller:
    def __init__(self, window, connector):
        self.window = window
        self.connector = connector
        self.login = None
        self.bind()

    def bind(self):
        self.window.connection_action.triggered.connect(self.show_login_dialog)
        self.window.databases.currentTextChanged.connect(self.populate_tree_view)

    def show_login_dialog(self):
        self.login = Login()
        self.login.setWindowTitle("Login")
        self.login.setGeometry(200, 200, 400, 200)
        self.login.submitClicked.connect(self.on_login_dialog_confirm)
        self.login.exec()

    def on_login_dialog_confirm(self, user, host, password):
        self.connector.test_connection(user, host, password)
        databases = self.connector.get_databases()
        self.window.databases.addItems(databases)

    def populate_tree_view(self, database):
        tree_model = self.create_model(self.window.schemas)
        self.window.schemas.setModel(tree_model)

        table_names = self.connector.get_tables(database)

        for table_name in table_names:
            self.add_tables(tree_model, table_name)

    @staticmethod
    def create_model(parent):
        model = QStandardItemModel(0, 0, parent)
        model.setHeaderData(0, Qt.Horizontal, "Schemas")
        return model

    @staticmethod
    def add_tables(model, table_name):
        model.insertRow(0)
        model.setData(model.index(0,0), table_name)