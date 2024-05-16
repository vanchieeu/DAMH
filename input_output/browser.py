from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import os

def linkto(main_window):
    link = QFileDialog.getOpenFileName(filter='*.jpg *.png')
    if link[0]:
        main_window.image_path = link[0]
        main_window.uic.screen.setPixmap(QPixmap(main_window.image_path))
        main_window.uic.line_Edit.setText(main_window.image_path)
        main_window.uic.label_2.show()
        main_window.uic.label.hide()
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            path = "image\\bo_loc_min\\" + str(i) + ".jpg"
            if os.path.isfile(path) == True:
                os.remove(path)
            path = "image\\bo_loc_sac_net\\" + str(i) + ".jpg"
            if os.path.isfile(path) == True:
                os.remove(path)
            path = "image\\bo_loc_tan_so\\" + str(i) + ".jpg"
            if os.path.isfile(path) == True:
                os.remove(path)
        main_window.uic.check_box.show()
