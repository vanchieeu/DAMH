import cv2
import os
from PyQt5.QtGui import QPixmap
from GUI.bo_loc_min import Ui_MainWindow3
from PyQt5 import QtCore, QtGui, QtWidgets
from convert_img_to_pixmap.convert_img_to_pixmap import convert_array_to_pixmap
from filter.time_domain_filter import Tich_chap, locTB, locTB_trong_so, locGaussian, loc_trung_vi, loc_max_min

def save_img(index, img):
    cv2.imwrite('image\\bo_loc_min\\' + str(index) + ".jpg", img)

def get_path(index):
    return "image\\bo_loc_min\\" + str(index) + ".jpg"

def handle_combobox_change_2(self, index):
    self.uic.save.show()
    img = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
    if self.uic.check_box_2.currentIndex() == 0:
        self.uic.save.hide()
        self.uic.screen.setPixmap(QPixmap(self.image_path))
    elif self.uic.check_box_2.currentIndex() == 1:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            b_channel, g_channel, r_channel = cv2.split(img)
            b_channel = Tich_chap(b_channel, locTB)
            g_channel = Tich_chap(g_channel, locTB)
            r_channel = Tich_chap(r_channel, locTB)
            imgTB = cv2.merge([b_channel, g_channel, r_channel])
            save_img(self.uic.check_box_2.currentIndex(), imgTB)
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
    elif self.uic.check_box_2.currentIndex() == 2:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            b_channel, g_channel, r_channel = cv2.split(img)
            b_channel = Tich_chap(b_channel, locTB_trong_so)
            g_channel = Tich_chap(g_channel, locTB_trong_so)
            r_channel = Tich_chap(r_channel, locTB_trong_so)
            imgTB_TS = cv2.merge([b_channel, g_channel, r_channel])
            save_img(self.uic.check_box_2.currentIndex(), imgTB_TS)
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
    elif self.uic.check_box_2.currentIndex() == 3:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            b_channel, g_channel, r_channel = cv2.split(img)
            b_channel = loc_trung_vi(b_channel)
            g_channel = loc_trung_vi(g_channel)
            r_channel = loc_trung_vi(r_channel)
            imgTV = cv2.merge([b_channel, g_channel, r_channel])
            save_img(self.uic.check_box_2.currentIndex(), imgTV)
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
    elif self.uic.check_box_2.currentIndex() == 4:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            b_channel, g_channel, r_channel = cv2.split(img)
            b_channel = Tich_chap(b_channel, locGaussian)
            g_channel = Tich_chap(g_channel, locGaussian)
            r_channel = Tich_chap(r_channel, locGaussian)
            imgGaussian = cv2.merge([b_channel, g_channel, r_channel])
            save_img(self.uic.check_box_2.currentIndex(), imgGaussian)
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
    elif self.uic.check_box_2.currentIndex() == 5:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            b_channel, g_channel, r_channel = cv2.split(img)
            b_channel = loc_max_min(b_channel, 1)
            g_channel = loc_max_min(b_channel, 1)
            r_channel = loc_max_min(b_channel, 1)
            imgMax = cv2.merge([b_channel, g_channel, r_channel])
            save_img(self.uic.check_box_2.currentIndex(), imgMax)
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
    elif self.uic.check_box_2.currentIndex() == 6:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            b_channel, g_channel, r_channel = cv2.split(img)
            b_channel = loc_max_min(b_channel, 2)
            g_channel = loc_max_min(b_channel, 2)
            r_channel = loc_max_min(b_channel, 2)
            imgMin = cv2.merge([b_channel, g_channel, r_channel])
            save_img(self.uic.check_box_2.currentIndex(), imgMin)
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))

def compare_change_2(self):
    for i in [1, 2, 3, 4, 5, 6, 0]:
        self.uic.check_box_2.setCurrentIndex(i)
        handle_combobox_change_2(self, i)
    set_screen_2(self)

def set_screen_2(self):
    self.MainWindow3 = QtWidgets.QMainWindow()
    self.ui = Ui_MainWindow3()
    self.ui.setupUi(self.MainWindow3)

    for index in [1, 2, 3, 4, 5, 6]:
        path = get_path(index)
        img = cv2.imread(path, 0)
        img = cv2.resize(src=img, dsize=(269, 259))
        pixmap = convert_array_to_pixmap(img)
        if index == 1:
            self.ui.screen_1.setPixmap(pixmap)
        elif index == 2:
            self.ui.screen_2.setPixmap(pixmap)
        elif index == 3:
            self.ui.screen_3.setPixmap(pixmap)
        elif index == 4:
            self.ui.screen_4.setPixmap(pixmap)
        elif index == 5:
            self.ui.screen_5.setPixmap(pixmap)
        elif index == 6:
            self.ui.screen_6.setPixmap(pixmap)

    self.MainWindow3.show()
