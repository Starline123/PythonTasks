from zad3 import *
import sys
#При открытие присутствуют поле значение 1 50 в поле 2 значение 100 в сумме результат просто лейблом а не кликом
#Сделать так чтобы
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Form()
ans = 0
def on_change():
    ui.lineEdit.setText(str(ui.znachenie1.value()))
    on_click()
def on_change2():
    ui.lineEdit_2.setText(str(ui.doubleSpinBox.value()))
    on_click()
def on_click():
    ui.label_3.setText("Сумма: " + str(ui.znachenie1.value() + ui.doubleSpinBox.value()))
ui.setupUi(MainWindow)
MainWindow.show()
#ui.label.setText("Новый текст")
ui.pushButton.clicked.connect(on_click)
ui.znachenie1.valueChanged.connect(on_change)
ui.doubleSpinBox.valueChanged.connect(on_change2)

sys.exit(app.exec_())