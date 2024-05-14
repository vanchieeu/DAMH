import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image, ImageOps
from GUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.browser.clicked.connect(self.linkto)
        self.uic.check_box.currentIndexChanged.connect(self.handle_combobox_change)
        self.uic.save.clicked.connect(self.save_img)

        self.image_path = None


    def save_img(self):
        if not self.uic.screen.pixmap():
            return

        # Open a save file dialog and allow the user to choose jpg or png
        path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "JPEG Files (*.jpg);;PNG Files (*.png)")

        if path:
            # Get the QPixmap from the QLabel
            pixmap = self.uic.screen.pixmap()

            # Convert QPixmap to QImage
            image = pixmap.toImage()

            # Determine the file extension from the path
            if path.endswith(".jpg"):
                image = image.convertToFormat(QImage.Format_RGB888)
                image.save(path, "JPEG")
            elif path.endswith(".png"):
                image.save(path, "PNG")


    def linkto(self):
        link = QFileDialog.getOpenFileName(filter='*.jpg *png')
        if link[0]:
            self.image_path = link[0]
            self.uic.screen.setPixmap(QPixmap(self.image_path))
            self.uic.line_Edit.setText(self.image_path)

    def handle_combobox_change(self, index):
        if index == 1 and self.image_path:
            self.qse()

    def qse(self):
        if not self.image_path:
            return

        # Open the image using Pillow
        image = Image.open(self.image_path)

        # Apply a grayscale filter (example of a time filter)
        image = ImageOps.grayscale(image)

        # Convert the processed image to QPixmap and display it
        qt_image = self.pil2pixmap(image)
        self.uic.screen.setPixmap(qt_image)

    def pil2pixmap(self, image):
        # Convert PIL image to QImage
        if image.mode == "RGB":
            r, g, b = image.split()
            image = Image.merge("RGB", (b, g, r))
        elif image.mode == "L":
            image = image.convert("RGB")
        data = image.tobytes("raw", "RGB")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())