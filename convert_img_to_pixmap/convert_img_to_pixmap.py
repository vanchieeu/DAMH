# image_utils.py
import numpy as np
from PyQt5.QtGui import QImage, QPixmap

def convert_array_to_pixmap(img_array: np.ndarray) -> QPixmap:
    height, width = img_array.shape
    bytes_per_line = width
    q_img = QImage(img_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
    pixmap = QPixmap.fromImage(q_img)
    return pixmap
