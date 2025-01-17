from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QGridLayout


class LoginWindow(QWidget):
    submitClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel("User: ", self)
        self.entry = QLineEdit(self)
        self.button = QPushButton("Send", self)
        self.button.clicked.connect(self.confirm)

        self.setCentralWidget(self)

        grid = QGridLayout()

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.entry, 0, 1)
        grid.addWidget(self.button, 1, 1)

        self.setLayout(grid)

    def confirm(self):
        self.submitClicked.emit(self.entry.text())
        self.close()