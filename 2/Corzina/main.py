from Corzina import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Form()
ans = 0
# Если больше 100 скидка 20% если выбран товар = 100 рублей то скидки не будет
def on_click():
    mysum =0
    if ui.checkBox.isChecked():
        mysum += 150
    if ui.checkBox_2.isChecked():
        mysum += 180
    if ui.checkBox_3.isChecked():
        mysum += 100
    if ui.checkBox_4.isChecked():
        mysum += 70
    if mysum > 100:
        mysum = mysum - mysum * 0.2
        ui.label_2.setText("Результат: " + str(mysum) + " + Скидка 20%")
    elif mysum == 100:
        ui.label_2.setText("Результат: " + str(mysum))
    else:
        ui.label_2.setText("Результат: " + str(mysum))
ui.setupUi(MainWindow)
MainWindow.show()
#ui.label.setText("Новый текст")
ui.pushButton.clicked.connect(on_click)

sys.exit(app.exec_())