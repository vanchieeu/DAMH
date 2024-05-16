import cv2
import os
from PyQt5.QtGui import QPixmap
from convert_img_to_pixmap.convert_img_to_pixmap import convert_array_to_pixmap
from filter.time_domain_filter import Tich_chap, locTB, locTB_trong_so, locGaussian, loc_trung_vi, loc_max_min

def save_img(index, img):
    cv2.imwrite('image\\bo_loc_min\\' + str(index) + ".jpg", img)

def get_path(index):
    return "image\\bo_loc_min\\" + str(index) + ".jpg"

def handle_combobox_change_2(self, index):
    self.uic.save.show()
    img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
    if self.uic.check_box_2.currentIndex() == 0:
        self.uic.save.hide()
        self.uic.screen.setPixmap(QPixmap(self.image_path))
    elif self.uic.check_box_2.currentIndex() == 1:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            imgTB = Tich_chap(img, locTB)
            pixmap = convert_array_to_pixmap(imgTB)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_2.currentIndex(), imgTB)
    elif self.uic.check_box_2.currentIndex() == 2:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            imgTB_TS = Tich_chap(img, locTB_trong_so)
            pixmap = convert_array_to_pixmap(imgTB_TS)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_2.currentIndex(), imgTB_TS)
    elif self.uic.check_box_2.currentIndex() == 3:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            imgTV = loc_trung_vi(img)
            pixmap = convert_array_to_pixmap(imgTV)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_2.currentIndex(), imgTV)
    elif self.uic.check_box_2.currentIndex() == 4:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            imgGaussian = Tich_chap(img, locGaussian)
            pixmap = convert_array_to_pixmap(imgGaussian)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_2.currentIndex(), imgGaussian)
    elif self.uic.check_box_2.currentIndex() == 5:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            imgMax = loc_max_min(img, 1)
            pixmap = convert_array_to_pixmap(imgMax)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_2.currentIndex(), imgMax)
    elif self.uic.check_box_2.currentIndex() == 6:
        if os.path.isfile(get_path(self.uic.check_box_2.currentIndex())) == True:
            self.uic.screen.setPixmap(QPixmap(get_path(self.uic.check_box_2.currentIndex())))
        else:
            imgMin = loc_max_min(img, 2)
            pixmap = convert_array_to_pixmap(imgMin)
            self.uic.screen.setPixmap(pixmap)
            save_img(self.uic.check_box_2.currentIndex(), imgMin)

def compare_change_2(self):
    for i in [1, 2, 3, 4, 5, 6, 0]:
        self.uic.check_box_2.setCurrentIndex(i)
        handle_combobox_change_2(self, i)