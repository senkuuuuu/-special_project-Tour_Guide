from PyQt5.QtWidgets import QMessageBox

class DialogBox(QMessageBox):
    def __init__(self, title:str, message:str):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle(title)
        self.setText(message)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

