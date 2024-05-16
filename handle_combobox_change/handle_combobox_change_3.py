import cv2
import os
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

