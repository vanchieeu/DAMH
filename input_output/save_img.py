from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage

def save_img(main_window):
    if not main_window.uic.screen.pixmap():
        return

    # Open a save file dialog and allow the user to choose jpg or png
    path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "JPEG Files (*.jpg);;PNG Files (*.png)")

    if path:
        # Get the QPixmap from the QLabel
        pixmap = main_window.uic.screen.pixmap()

        # Convert QPixmap to QImage
        image = pixmap.toImage()

        # Determine the file extension from the path
        if path.endswith(".jpg"):
            image = image.convertToFormat(QImage.Format_RGB888)
            image.save(path, "JPEG")
        elif path.endswith(".png"):
            image.save(path, "PNG")
