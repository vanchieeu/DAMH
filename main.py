import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from input_output import browser, save_img
from GUI.GUI import Ui_MainWindow
from handle_combobox_change.handle_combobox_change import handle_combobox_change

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.browser.clicked.connect(lambda: browser.linkto(self))
        self.uic.check_box_2.hide()
        self.uic.check_box.currentIndexChanged.connect(lambda index: handle_combobox_change(self, index))
        self.uic.save.clicked.connect(lambda: save_img.save_img(self))

        self.image_path = None

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())