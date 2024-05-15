import cv2     # Thư viện OpenCV
import numpy as np   # Thư viện numy để làm việc dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh

# Định nghĩa hàm Tich_chap() để lọc Trung bình, Trung bình có trọng số và lọc Gaussian
def Tich_chap(img,mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp   =  img[i-1, j-1]    * mask[0, 0]\
                   +  img[i, j-1]      * mask[0, 1]\
                   +  img[i+1, j - 1]  * mask[0, 2]\
                   +  img[i-1, j]      * mask[1, 0]\
                   +  img[i, j]        * mask[1, 1]\
                   +  img[i+1, j]      * mask[1, 2]\
                   +  img[i - 1, j+1]  * mask[2, 0]\
                   +  img[i, j + 1]    * mask[2, 1]\
                   +  img[i + 1, j + 1]* mask[2, 2]
            img_new[i, j]= temp
    img_new = img_new.astype(np.uint8)
    return img_new

# Định nghĩa bộ lọc Laplacian chuẩn
locLaplacian_chuan = np.array(([0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]), dtype="float")

# Định nghĩa bộ lọc Laplacian biến thể 1
locLaplacian_Bien_The_1 = np.array(([1, 1, 1],
                                    [1, -8, 1],
                                    [1, 1, 1]), dtype="float")

# Định nghĩa bộ lọc Laplacian biến thể 2
locLaplacian_Bien_The_2 = np.array(([0, -1, 0],
                                    [-1, 4, -1],
                                    [0, -1, 0]), dtype="float")

# Định nghĩa bộ lọc Laplacian biến thể 3
locLaplacian_Bien_The_3 = np.array(([-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]), dtype="float")


locLaplacian_Cai_Thien = np.array(([-1, -1, -1],
                                    [-1, 5, -1],
                                    [-1, -1, -1]), dtype="float")