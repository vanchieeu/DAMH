import cv2     # Thư viện OpenCV
import numpy as np   # Thư viện numy để làm việc dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh

def Tich_chap(img, mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp   =  img[i-1, j-1]    * mask[0, 0]\
                   +  img[i-1, j]      * mask[0, 1]\
                   +  img[i-1, j + 1]  * mask[0, 2]\
                   +  img[i, j-1]      * mask[1, 0]\
                   +  img[i, j]        * mask[1, 1]\
                   +  img[i, j + 1]    * mask[1, 2]\
                   +  img[i + 1, j-1]  * mask[2, 0]\
                   +  img[i + 1, j]    * mask[2, 1]\
                   +  img[i + 1, j + 1]* mask[2, 2]
            img_new[i, j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new

# Định nghĩa bộ lọc trung bình
locTB = np.array(([1/9, 1/9, 1/9],
                  [1/9, 1/9, 1/9],
                  [1/9, 1/9, 1/9]), dtype="float")

# Định nghĩa bộ lọc trung bình có trọng số
locTB_trong_so = np.array(([1/16, 2/16, 1/16],
                           [2/16, 4/16, 2/16],
                           [1/16, 2/16, 1/16]), dtype="float")

locGaussian = np.array(([0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976],
                        [0.1238/4.8976, 0.2042/4.8976, 0.1238/4.8976],
                        [0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976]), dtype="float")

def loc_trung_vi(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]

            temp = sorted(temp)
            img_new[i, j] = temp[4]
    img_new = img_new.astype(np.uint8)
    return img_new

def loc_max_min(img, index):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]

            if index == 1:
                temp = max(temp)
            else:
                temp = min(temp)
            img_new[i, j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new