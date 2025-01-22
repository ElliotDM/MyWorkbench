"""
Created on Mon Jan 20 2025

@Author: Elliot
"""


from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QDialog,
    QPushButton, 
    QLineEdit, 
    QLabel, 
    QVBoxLayout)


class Login(QDialog):
    submitClicked = pyqtSignal(str, str, str)

    def __init__(self):
        super().__init__()

        self.user = QLabel("User: ")
        self.user_entry = QLineEdit()

        self.host = QLabel("Host: ")
        self.host_entry = QLineEdit()

        self.password = QLabel("Password: ")
        self.password_entry = QLineEdit()

        self.button = QPushButton("Send")
        self.button.clicked.connect(self.confirm)

        layout = QVBoxLayout(self)
        layout.addWidget(self.user)
        layout.addWidget(self.user_entry)
        layout.addWidget(self.host)
        layout.addWidget(self.host_entry)
        layout.addWidget(self.password)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.button)

    def confirm(self):
        self.submitClicked.emit(
            self.user_entry.text(),
            self.host_entry.text(),
            self.password_entry.text()
        )
        self.close()