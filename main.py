import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from input_output import browser, save_img
from GUI import Ui_MainWindow
from handle_combobox_change_2.handle_combobox_change_2 import handle_combobox_change_2

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.browser.clicked.connect(lambda: browser.linkto(self))
        self.uic.check_box_2.hide()
        self.uic.check_box.currentIndexChanged.connect(self.handle_combobox_change)
        self.uic.save.clicked.connect(lambda: save_img.save_img(self))

        self.image_path = None
        if self.image_path == None:
            self.uic.check_box.hide()
            self.uic.label_2.hide()

    def handle_combobox_change(self, index):
        self.uic.check_box_2.hide()
        if index == 0:
            self.uic.screen.setPixmap(QPixmap(self.image_path))
        if index == 1:
            self.uic.screen.setPixmap(QPixmap("C:\\Users\\chieu\\OneDrive\\Pictures\\b.jpg"))
        if index == 2:
            self.uic.check_box_2.show()
            self.uic.screen.setPixmap(QPixmap(self.image_path))
            self.uic.check_box_2.currentIndexChanged.connect(lambda idx: handle_combobox_change_2(self, idx))

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())