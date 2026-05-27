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
        # get input from input box
        user_input = self.txtBox.text()

        # add to the list widget
        self.list.addItem(user_input)

        # clear
        self.txtBox.setText("")


    def delete(self):
        # get row of the task
        row = self.list.currentRow()

        # obtain selected task from list widget and delete
        task = self.list.takeItem(row)
        del task