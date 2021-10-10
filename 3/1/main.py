from mainwindow import *
from dialog import *
import sys
#first form
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
uimainwnd = Ui_MainWindow()
#Second form
Dialog = QtWidgets.QDialog()
uidialog = Ui_Dialog()


def mbtn1_click():
    if uimainwnd.lineEdit.text() != "":
        uimainwnd.listWidget.addItem(uimainwnd.lineEdit.text())
        print("currentItem " + str(uimainwnd.listWidget.currentItem()))
        print("currentRow " + str(uimainwnd.listWidget.currentRow()))
        print("currentIndex " + str(uimainwnd.listWidget.currentIndex()))
        print("selectedItems " + str(uimainwnd.listWidget.selectedItems()))
        print("selectedIndexes " + str(uimainwnd.listWidget.selectedIndexes()))


def mbtn2_click():
    sel_item = uimainwnd.listWidget.selectedItems()

    for item in sel_item:
        uidialog.lineEdit.setText(item.text())
    Dialog.show()


def mbtn3_click():
    uimainwnd.listWidget.takeItem(uimainwnd.listWidget.currentRow())

def mbtn4_click():
    uimainwnd.listWidget.clear()


def mlw_click():
    sel_item = uimainwnd.listWidget.selectedItems()

    for item in sel_item:
        uidialog.lineEdit.setText(item.text())

def dbtn1_click():
    sel_item = uimainwnd.listWidget.selectedItems()

    for item in sel_item:
        item.setText(uidialog.lineEdit.text())

def dbtn2_click():
    Dialog.hide()

uimainwnd.setupUi(MainWindow)
MainWindow.show()
#Setup dialog ui but do not show it
uidialog.setupUi(Dialog)
#Form1 Funcs
uimainwnd.pushButton.clicked.connect(mbtn1_click)
uimainwnd.pushButton_2.clicked.connect(mbtn2_click)
uimainwnd.pushButton_3.clicked.connect(mbtn3_click)
uimainwnd.pushButton_4.clicked.connect(mbtn4_click)
uimainwnd.listWidget.clicked.connect(mlw_click)
#Form2 Funcs
uidialog.pushButton.clicked.connect(dbtn1_click)
uidialog.pushButton_2.clicked.connect(dbtn2_click)

sys.exit(app.exec_())