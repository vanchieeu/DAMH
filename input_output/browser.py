from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

def linkto(main_window):
    link = QFileDialog.getOpenFileName(filter='*.jpg *.png')
    if link[0]:
        main_window.image_path = link[0]
        main_window.uic.screen.setPixmap(QPixmap(main_window.image_path))
        main_window.uic.line_Edit.setText(main_window.image_path)
        main_window.uic.label_2.show()
        main_window.uic.label.hide()
        main_window.uic.check_box.show()
