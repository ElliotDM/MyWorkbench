import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from controller import MainController
from connector import Connector

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    connector = Connector()
    controller = MainController(window, connector)
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()