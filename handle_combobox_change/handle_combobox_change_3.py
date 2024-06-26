import cv2
import os
import sys
import numpy as np
from GUI.bo_loc_sac_net import Ui_MainWindow2
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from convert_img_to_pixmap.convert_img_to_pixmap import convert_array_to_pixmap
from filter.robert_cross_gradient_filter import Tich_chap, loc_Robert_Cross1, loc_Robert_Cross2
from filter.sobel_filter import Tich_chap, locSobelX, locSobelY
from filter.laplacian_filter import Tich_chap, locLaplacian_chuan, locLaplacian_Cai_Thien, locLaplacian_Bien_The_1, locLaplacian_Bien_The_2, locLaplacian_Bien_The_3

def save_img(index, img):
    cv2.imwrite('image\\bo_loc_sac_net\\' + str(index) + ".jpg", img)

def get_path(index):
    return "image\\bo_loc_sac_net\\" + str(index) + ".jpg"

def handle_combobox_change_3(self, index):
    self.uic.save.show()
    img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
    if self.uic.check_box_3.currentIndex() == 0:
        self.uic.save.hide()
        self.uic.screen.setPixmap(QPixmap(self.image_path))
    elif self.uic.check_box_3.currentIndex() == 3:
        if os.path.isfile(get_path(self.uic.check_box_3.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_3.currentIndex())))
        else:
            img_Robert_Cross1 = Tich_chap(img, loc_Robert_Cross1)
            img_Robert_Cross2 = Tich_chap(img, loc_Robert_Cross2)
            img_Robert_Cross_result = img_Robert_Cross1 + img_Robert_Cross2 + img
            pixmap = convert_array_to_pixmap(img_Robert_Cross_result)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_3.currentIndex(), img_Robert_Cross_result)
    elif self.uic.check_box_3.currentIndex() == 1:
        if os.path.isfile(get_path(self.uic.check_box_3.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_3.currentIndex())))
        else:
            img_loc_Laplacian_chuan = Tich_chap(img, locLaplacian_chuan)
            img_cai_thien_locLaplacian_chuan = img - img_loc_Laplacian_chuan
            pixmap = convert_array_to_pixmap(img_cai_thien_locLaplacian_chuan)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_3.currentIndex(), img_cai_thien_locLaplacian_chuan)
    elif self.uic.check_box_3.currentIndex() == 4:
        if os.path.isfile(get_path(self.uic.check_box_3.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_3.currentIndex())))
        else:
            imgSobelX = Tich_chap(img, locSobelX)
            imgSobelY = Tich_chap(img, locSobelY)
            imgSobel_result = imgSobelX + imgSobelY + img
            pixmap = convert_array_to_pixmap(imgSobel_result)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_3.currentIndex(), imgSobel_result)
    elif self.uic.check_box_3.currentIndex() == 2:
        if os.path.isfile(get_path(self.uic.check_box_3.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_3.currentIndex())))
        else:
            img_loc_Laplacian_Bien_The_1 = Tich_chap(img, locLaplacian_Bien_The_1)
            img_cai_thien_loc_Laplacian_Bien_The_1 = img - img_loc_Laplacian_Bien_The_1
            pixmap = convert_array_to_pixmap(img_cai_thien_loc_Laplacian_Bien_The_1)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_3.currentIndex(), img_cai_thien_loc_Laplacian_Bien_The_1)

def compare_change_3(self):
    for i in [1, 2, 3, 4, 0]:
        self.uic.check_box_3.setCurrentIndex(i)
        handle_combobox_change_3(self, i)
    set_screen_2(self)

def set_screen_2(self):
    self.MainWindow2 = QtWidgets.QMainWindow()
    self.ui = Ui_MainWindow2()
    self.ui.setupUi(self.MainWindow2)

    for index in [1, 2, 3, 4]:
        path = get_path(index)
        img = cv2.imread(path, 0)
        img = cv2.resize(src=img, dsize=(self.ui.screen_4.geometry().width(), self.ui.screen_1.geometry().height()))
        pixmap = convert_array_to_pixmap(img)
        if index == 1:
            self.ui.screen_1.setPixmap(pixmap)
        elif index == 2:
            self.ui.screen_2.setPixmap(pixmap)
        elif index == 3:
            self.ui.screen_3.setPixmap(pixmap)
        elif index == 4:
            self.ui.screen_4.setPixmap(pixmap)

    self.MainWindow2.show()


