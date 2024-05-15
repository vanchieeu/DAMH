import cv2
from PyQt5.QtGui import QPixmap
from convert_img_to_pixmap.convert_img_to_pixmap import convert_array_to_pixmap
from filter.time_domain_filter import Tich_chap, locTB, locTB_trong_so, locGaussian, loc_trung_vi, loc_max_min
import matplotlib.pyplot as plt

def handle_combobox_change_2(self, index):
    self.uic.save.show()
    img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
    if self.uic.check_box_2.currentIndex() == 0:
        self.uic.save.hide()
        self.uic.screen.setPixmap(QPixmap(self.image_path))
    elif self.uic.check_box_2.currentIndex() == 1:
        imgTB = Tich_chap(img, locTB)
        pixmap = convert_array_to_pixmap(imgTB)
        self.uic.screen.setPixmap(pixmap)
    elif self.uic.check_box_2.currentIndex() == 2:
        imgTB_TS = Tich_chap(img, locTB_trong_so)
        pixmap = convert_array_to_pixmap(imgTB_TS)
        self.uic.screen.setPixmap(pixmap)
    elif self.uic.check_box_2.currentIndex() == 3:
        imgTV = loc_trung_vi(img)
        pixmap = convert_array_to_pixmap(imgTV)
        self.uic.screen.setPixmap(pixmap)
    elif self.uic.check_box_2.currentIndex() == 4:
        imgGaussian = Tich_chap(img, locGaussian)
        pixmap = convert_array_to_pixmap(imgGaussian)
        self.uic.screen.setPixmap(pixmap)
    elif self.uic.check_box_2.currentIndex() == 5:
        imgMax = loc_max_min(img, 1)
        pixmap = convert_array_to_pixmap(imgMax)
        self.uic.screen.setPixmap(pixmap)
    elif self.uic.check_box_2.currentIndex() == 6:
        imgMin = loc_max_min(img, 2)
        pixmap = convert_array_to_pixmap(imgMin)
        self.uic.screen.setPixmap(pixmap)