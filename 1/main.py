from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def show():
    Form, Window = uic.loadUiType("dialog.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec()

if __name__ == '__main__':
    show()