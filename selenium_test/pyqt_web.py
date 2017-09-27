# -*- coding: utf-8 -*-

#
# Created: Py40.com Feb 20 10:03:54 2017
#      by: PyQt5
#

from PyQt4.QtGui import QApplication, QWidget, QPushButton,QDesktopWidget,QLabel,QGridLayout

import webbrowser,sys


# class Ui_MainWindow(QWidget):
#     item_name = "PyQt打开外部链接"

#     def __init__(self):
#         super(int).__init__(int)
#         initUI()

#     def initUI(self):
#         tips_1 = QLabel("网站：<a href='http://code.py40.com'>http://code.py40.com</a>");
#         tips_1.setOpenExternalLinks(True)

#         btn_webbrowser = QPushButton('webbrowser效果', self)

#         btn_webbrowser.clicked.connect(btn_webbrowser_Clicked)

#         grid = QGridLayout()
#         grid.setSpacing(10)

#         grid.addWidget(btn_webbrowser, 1, 0)
#         grid.addWidget(tips_1, 2, 0)

#         setLayout(grid)

#         resize(250, 150)
#         setMinimumSize(266, 304);
#         setMaximumSize(266, 304);
#         center()
#         setWindowTitle(item_name)
#         show()


    # def btn_webbrowser_Clicked(self):
    #     webbrowser.open('http://www.paoquba.com/')


    # def center(self):
    #     qr = frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # a = Ui_MainWindow()
    tips_1 = QLabel("网站：<a href='http://code.py40.com'>http://code.py40.com</a>");
    tips_1.setOpenExternalLinks(True)

    # btn_webbrowser = QPushButton('webbrowser效果', self)

    # btn_webbrowser.clicked.connect(btn_webbrowser_Clicked)

    grid = QGridLayout()
    grid.setSpacing(10)

    # grid.addWidget(btn_webbrowser, 1, 0)
    grid.addWidget(tips_1, 2, 0)




    item_name = "PyQt打开外部链接"

    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.resize(250, 150)
    main_frame.setMinimumSize(266, 304);
    main_frame.setMaximumSize(266, 304);
    # main_frame.center()
    main_frame.setWindowTitle(item_name)
    main_frame.show()
    sys.exit(app.exec_())