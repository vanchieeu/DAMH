from PyQt5.QtGui import QPixmap

def handle_combobox_change(main_window, index):
    main_window.uic.check_box_2.hide()
    if index == 0:
        main_window.uic.screen.setPixmap(QPixmap(main_window.image_path))
    elif index == 1:
        main_window.uic.screen.setPixmap(QPixmap("C:\\Users\\chieu\\OneDrive\\Pictures\\b.jpg"))
    elif index == 2:
        main_window.uic.check_box_2.show()
        main_window.uic.screen.setPixmap(QPixmap(main_window.image_path))
        main_window.uic.check_box_2.currentIndexChanged.connect(lambda index: handle_combobox_change_2(main_window, index))

def handle_combobox_change_2(main_window, index):
    pass
