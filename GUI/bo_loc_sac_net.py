# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bo_loc_sac_net.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(869, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.screen_1 = QtWidgets.QLabel(self.centralwidget)
        self.screen_1.setGeometry(QtCore.QRect(20, 40, 391, 230))
        self.screen_1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen_1.setText("")
        self.screen_1.setObjectName("screen_1")
        self.screen_2 = QtWidgets.QLabel(self.centralwidget)
        self.screen_2.setGeometry(QtCore.QRect(459, 40, 391, 230))
        self.screen_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen_2.setText("")
        self.screen_2.setObjectName("screen_2")
        self.screen_4 = QtWidgets.QLabel(self.centralwidget)
        self.screen_4.setGeometry(QtCore.QRect(459, 320, 391, 230))
        self.screen_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen_4.setText("")
        self.screen_4.setObjectName("screen_4")
        self.screen_3 = QtWidgets.QLabel(self.centralwidget)
        self.screen_3.setGeometry(QtCore.QRect(20, 320, 391, 230))
        self.screen_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen_3.setText("")
        self.screen_3.setObjectName("screen_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 290, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(640, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "So sánh bộ lọc mịn"))
        self.label_5.setText(_translate("MainWindow2", "Laplacian chuẩn"))
        self.label_6.setText(_translate("MainWindow2", "Laplacian biến thể"))
        self.label_7.setText(_translate("MainWindow2", "Robert Cross Gradient"))
        self.label_8.setText(_translate("MainWindow2", "Sobel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())