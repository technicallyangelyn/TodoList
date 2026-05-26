from PyQt6.QtWidgets import QMainWindow
from gui import Ui_TodoList


class Logic(QMainWindow, Ui_TodoList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #make window non-resizable
        self.setFixedSize(524, 353)

        #connecting buttons to functions
        self.addButton.clicked.connect(self.add)
        self.deleteButton.clicked.connect(self.delete)


    def add(self):
        pass


    def delete(self):
        pass