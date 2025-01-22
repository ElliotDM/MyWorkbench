"""
Created on Wed Jan 15 2025

@Author: Elliot
"""


from PyQt5.QtWidgets import (
    QMainWindow,
    QAction,
    QComboBox,
    QToolBar,
    QTreeView,
    QTextEdit,
    QStatusBar,
    QWidget,
    QGridLayout)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyWorkbench")

        self.connection_action = QAction(QIcon("./assets/connect.png"),
                                            "Connect", self)
        self.connection_action.setStatusTip("Connect to database")

        self.disconnection_action = QAction(QIcon("./assets/disconnect.png"),
                                       "Disconnect", self)
        self.disconnection_action.setStatusTip("Disconnect from database")

        self.run_action = QAction(QIcon("./assets/run.png"),
                                       "Run", self)
        self.run_action.setStatusTip("Run script")

        self.stop_action = QAction(QIcon("./assets/stop.png"),
                             "Stop", self)
        self.stop_action.setStatusTip("Stop script")

        self.undo_action = QAction(QIcon("./assets/undo.png"),
                              "Undo", self)
        self.undo_action.setStatusTip("Undo")

        self.redo_action = QAction(QIcon("./assets/redo.png"),
                              "Redo", self)
        self.redo_action.setStatusTip("Redo")

        self.new_file_action = QAction(QIcon("./assets/file.png"),
                              "New file", self)
        self.new_file_action.setStatusTip("New File")

        self.open_file_action = QAction(QIcon("./assets/folder.png"),
                                  "Open file", self)
        self.open_file_action.setStatusTip("Open File")

        self.save_action = QAction(QIcon("./assets/save.png"),
                                   "Save file", self)
        self.save_action.setStatusTip("Save File")

        self.save_as_action = QAction(QIcon("./assets/save_as.png"),
                              "Save as...", self)
        self.save_as_action.setStatusTip("Save as...")

        self.search_action = QAction(QIcon("./assets/search.png"),
                                 "Search", self)
        self.search_action.setStatusTip("Search")

        self.databases = QComboBox(self)

        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)

        self.toolbar.addWidget(self.databases)
        self.toolbar.addAction(self.connection_action)
        self.toolbar.addAction(self.disconnection_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.run_action)
        self.toolbar.addAction(self.stop_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.undo_action)
        self.toolbar.addAction(self.redo_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.new_file_action)
        self.toolbar.addAction(self.open_file_action)
        self.toolbar.addAction(self.save_action)
        self.toolbar.addAction(self.save_as_action)
        self.toolbar.addAction(self.search_action)

        self.schemas = QTreeView(self)
        self.text_editor = QTextEdit(self)
        self.table = QTreeView(self)

        self.status_bar = QStatusBar(self)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid = QGridLayout()

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 5)
        grid.setRowStretch(0,3)
        grid.setRowStretch(1,3)

        grid.addWidget(self.schemas, 0, 0)
        grid.addWidget(self.text_editor, 0, 1)
        grid.addWidget(self.table, 1, 1)

        central_widget.setLayout(grid)
        self.showMaximized()