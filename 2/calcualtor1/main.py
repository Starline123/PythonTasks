from calculator import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Form()
ans = 0
def on_click():
    if not ui.lineEdit.text() == "" and not ui.lineEdit_2.text() == "":
        if ui.radioButton.isChecked():
            ans = int(ui.lineEdit.text()) + int(ui.lineEdit_2.text())
            ui.label_3.setText("Результат: " + str(ans))
        elif ui.radioButton_2.isChecked():
            ans = int(ui.lineEdit.text()) - int(ui.lineEdit_2.text())
            ui.label_3.setText("Результат: " + str(ans))
        elif ui.radioButton_3.isChecked():
            ans = int(ui.lineEdit.text()) * int(ui.lineEdit_2.text())
            ui.label_3.setText("Результат: " + str(ans))
        elif ui.radioButton_4.isChecked():
            print(int(ui.lineEdit_2.text()))
            if int(ui.lineEdit_2.text()) == 0:
                print(int(ui.lineEdit_2.text()))
                ui.label_3.setText("Результат: ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ")
            else:
                ans = int(ui.lineEdit.text()) / int(ui.lineEdit_2.text())
                ui.label_3.setText("Результат: " + str(ans))
ui.setupUi(MainWindow)
MainWindow.show()
#ui.label.setText("Новый текст")
ui.pushButton.clicked.connect(on_click)

sys.exit(app.exec_())