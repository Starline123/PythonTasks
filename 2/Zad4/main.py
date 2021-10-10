from zad4 import *
import sys
#Чтобы когда сний когда (вертикальный) веддем вверх другой сини вправо
#Серый вертикальный вверх серый горизонтальный влево
#Синий с синими серый с серыми
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Form()
ans = 0
def hScBar():
    #ui.horizontalSlider.setValue(ui.horizontalScrollBar.value())
    ui.verticalScrollBar.setValue(ui.horizontalScrollBar.value())
    ui.lineEdit.setText(str(ui.horizontalScrollBar.value()) + " | " + str(ui.horizontalSlider.value()))
def hSl():
    #ui.horizontalScrollBar.setValue(ui.horizontalSlider.value())
    ui.verticalSlider.setValue(ui.horizontalSlider.value())
    ui.lineEdit.setText(str(ui.horizontalScrollBar.value()) + " | " + str(ui.horizontalSlider.value()))
def vScBar():
    #ui.verticalSlider.setValue(ui.verticalScrollBar.value())
    ui.horizontalScrollBar.setValue(ui.verticalScrollBar.value())
    ui.lineEdit.setText(str(ui.horizontalScrollBar.value()) + " | " + str(ui.horizontalSlider.value()))
def vSl():
    #ui.verticalScrollBar.setValue(ui.verticalSlider.value())
    ui.horizontalSlider.setValue(ui.verticalSlider.value())
    ui.lineEdit.setText(str(ui.horizontalScrollBar.value()) + " | " + str(ui.horizontalSlider.value()))
ui.setupUi(MainWindow)
MainWindow.show()
ui.horizontalScrollBar.valueChanged.connect(hScBar)
ui.horizontalSlider.valueChanged.connect(hSl)
ui.verticalScrollBar.valueChanged.connect(vScBar)
ui.verticalSlider.valueChanged.connect(vSl)

sys.exit(app.exec_())