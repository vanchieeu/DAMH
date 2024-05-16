import cv2
import numpy as np
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from convert_img_to_pixmap.convert_img_to_pixmap import convert_array_to_pixmap
from filter.butterworth_thong_cao_filter import DFT1D, IDFT1D, butterworthHP


def handle_combobox_change_4(self, index):
    self.uic.save.show()
    img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(src=img, dsize=(100, 100))
    if self.uic.check_box_4.currentIndex() == 0:
        self.uic.save.hide()
        self.uic.screen.setPixmap(QPixmap(self.image_path))
    elif self.uic.check_box_4.currentIndex() == 1:
        f = np.asarray(img)
        M, N = np.shape(f)

        # Bước 1: Chuyển ảnh từ kích thước MxN vào ảnh PxQ với P= 2M và Q =2N
        P, Q = 2 * M, 2 * N
        shape = np.shape(f)
        # Chuyển ảnh PxQ vào mảng fp
        f_xy_p = np.zeros((P, Q), dtype = 'complex_')
        f_xy_p[:shape[0], :shape[1]] = f

        # Bước 2: Nhân ảnh fp(x,y) với (-1) mũ (x+y) để tạo ảnh mới
        # Kết quả nhân lưu vào ma trận ảnh fpc
        F_xy_p = np.zeros((P, Q), dtype = 'complex_')
        for x in range(P):
            for y in range(Q):
                F_xy_p[x, y] = f_xy_p[x, y] * np.power(-1, x + y)

        # Bước 3: Chuyển đổi ảnh Fpc sang miền tần số (DFT)
        dft_cot = dft_hang = np.zeros((P, Q), dtype = 'complex_')
        # DFT theo P - cột
        for i in range(P):
            dft_cot[i] = DFT1D(F_xy_p[i])
        # DFT theo Q - hàng
        for j in range(Q):
            dft_hang[:, j] = DFT1D(dft_cot[:, j])

        # Bước 4: Gọi hàm butterworthHP tạo bộ lọc thông cao butterworth
        H_uv = butterworthHP(60, P, Q, 2)

        # Bước 5: Nhân ảnh sau khi DFT với ảnh sau khi lọc
        G_uv = np.multiply(dft_hang, H_uv)

        # Bước 6:
        # Bước 6.1 Thực hiện biến đổi ngược DFT
        idft_cot = idft_hang = np.zeros((P, Q), dtype = 'complex_')
        # chuyển đổi DFT ngược theo P - cột
        for i in range(P):
            idft_cot[i] = IDFT1D(G_uv[i])
        # Chuyển đổi DFT ngược theo Q - hàng
        for j in range(Q):
            idft_hang[:, j] = IDFT1D(idft_cot[:, j])

        # Bước 6.2: Nhân phần thực ảnh sau khi biến đổi ngược với -1 mũ (x+y)
        g_array = np.asarray(idft_hang.real)
        P, Q = np.shape(g_array)
        g_xy_p = np.zeros((P, Q), dtype = 'complex_')
        for x in range(P):
            for y in range(Q):
                g_xy_p[x, y] = g_array[x, y] * np.power(-1, x + y)

        # Bước 7: Rút trích ảnh kích thước MxN từ ảnh PxQ
        # Và đây ảnh cuối cùng sau khi lọc
        g_xy = g_xy_p[:shape[0], :shape[1]]

        img_new = g_xy.astype(np.uint8)
        pixmap = convert_array_to_pixmap(img_new)
        self.uic.screen.setPixmap(pixmap)
    elif self.uic.check_box_4.currentIndex() == 2:
        print("2")
    elif self.uic.check_box_4.currentIndex() == 3:
        print("3")
    elif self.uic.check_box_4.currentIndex() == 4:
        print("4")

def compare_change_4(self):
    for i in [1, 2, 3, 4, 0]:
        self.uic.check_box_4.setCurrentIndex(i)
        handle_combobox_change_4(self, i)