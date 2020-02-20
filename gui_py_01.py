import sys
from PyQt5 import QtCore, QtWidgets, uic

form_class = uic.loadUiType('/Users/midou/Desktop/pylearnfiles/excellearn_data/tempconv.ui')[0] #获取gui——mainwindow

class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__ (self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btn_CtoF_clicked)    #绑定按钮的时间处理器
        self.btnFtoC.clicked.connect(self.btn_FtoC_clicked)

    def btn_CtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel * 9 / 5.0 + 32
        self.spinFahr.setValue(int(fahr + 0.5))

    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = round((fahr - 32) * 5 / 9.0, 2)
        self.editCel.setText(str(cel))

app = QtWidgets.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
