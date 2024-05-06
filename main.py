import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog
from GUI import Ui_MainWindow
from PyQt5.QtGui import QPixmap

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.browser.clicked.connect(self.linkto)


    def linkto(self):
        link = QFileDialog.getOpenFileName(filter='*.jpg *png')
        self.uic.screen.setPixmap(QPixmap(link[0]))
        self.uic.line_Edit.setText(link[0])


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())