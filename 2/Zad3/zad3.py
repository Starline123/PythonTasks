# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\zad3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(275, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.znachenie1 = QtWidgets.QSpinBox(Form)
        self.znachenie1.setGeometry(QtCore.QRect(80, 10, 61, 22))
        self.znachenie1.setMaximum(99999)
        self.znachenie1.setProperty("value", 50)
        self.znachenie1.setObjectName("znachenie1")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(80, 40, 62, 22))
        self.doubleSpinBox.setMaximum(100000.99)
        self.doubleSpinBox.setProperty("value", 100.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 100, 111, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Значение 1"))
        self.label_2.setText(_translate("Form", "Значение 2"))
        self.lineEdit.setText(_translate("Form", "50"))
        self.lineEdit_2.setText(_translate("Form", "100,00"))
        self.label_3.setText(_translate("Form", "Сумма: 150"))
        self.pushButton.setText(_translate("Form", "Рассчитать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
