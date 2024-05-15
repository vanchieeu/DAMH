# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browser = QtWidgets.QPushButton(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(250, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browser.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/browser-icon-image.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browser.setIcon(icon)
        self.browser.setObjectName("browser")
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(20, 100, 641, 341))
        self.screen.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen.setText("")
        self.screen.setScaledContents(True)
        self.screen.setObjectName("screen")
        self.check_box = QtWidgets.QComboBox(self.centralwidget)
        self.check_box.setGeometry(QtCore.QRect(120, 50, 141, 31))
        self.check_box.setObjectName("check_box")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.check_box.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.line_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Edit.setGeometry(QtCore.QRect(20, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.line_Edit.setFont(font)
        self.line_Edit.setObjectName("line_Edit")
        self.check_box_2 = QtWidgets.QComboBox(self.centralwidget)
        self.check_box_2.setGeometry(QtCore.QRect(270, 50, 161, 31))
        self.check_box_2.setObjectName("check_box_2")
        self.check_box_2.addItem("")
        self.check_box_2.addItem("")
        self.check_box_2.addItem("")
        self.check_box_2.addItem("")
        self.check_box_2.addItem("")
        self.check_box_2.addItem("")
        self.check_box_2.addItem("")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(570, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/save-icon-png-image.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon1)
        self.save.setObjectName("save")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.compare = QtWidgets.QPushButton(self.centralwidget)
        self.compare.setGeometry(QtCore.QRect(350, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.compare.setFont(font)
        self.compare.setObjectName("compare")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browser.setText(_translate("MainWindow", "Browser"))
        self.check_box.setItemText(0, _translate("MainWindow", "None"))
        self.check_box.setItemText(1, _translate("MainWindow", "Bộ lọc tần số"))
        self.check_box.setItemText(2, _translate("MainWindow", "Bộ lọc thời gian"))
        self.label_2.setText(_translate("MainWindow", "Choose filter"))
        self.check_box_2.setItemText(0, _translate("MainWindow", "None"))
        self.check_box_2.setItemText(1, _translate("MainWindow", "Trung bình"))
        self.check_box_2.setItemText(2, _translate("MainWindow", "Trung bình có trọng số"))
        self.check_box_2.setItemText(3, _translate("MainWindow", "Trung vị"))
        self.check_box_2.setItemText(4, _translate("MainWindow", "Gaussian"))
        self.check_box_2.setItemText(5, _translate("MainWindow", "Max"))
        self.check_box_2.setItemText(6, _translate("MainWindow", "Min"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Please choose one picture"))
        self.compare.setText(_translate("MainWindow", "Compare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
