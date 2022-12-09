# # import requests
# from Lib.crawler import Crawler
# # import os
# from Lib.db import DB
# import sys


import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from Lib.crawler import Crawler
from Lib.PyQT import TableViewWidget
from Lib.db import DB

from PyQt5.QtGui import QPixmap

MAIN_PAGE_PATH = "/chart/moviemeter/?ref_=nv_mv_mpm"


class MainWindow(qtw.QMainWindow):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('IMDB Crawler')
        self.setWindowIcon(qtg.QIcon('Lib/imdb_logo.png'))


        ### Main layout
        mainLayout = qtw.QVBoxLayout()

        ### Table Caption part:
        lblTableCaption = qtw.QLabel('IMDB Data')  # ????????????????
        pixmap = QPixmap('Lib/imdb_pic.jpg')
        lblTableCaption.setPixmap(pixmap)
        lblTableCaption.setObjectName('lblTableCaption')
        lblTableCaption.setAlignment(qtc.Qt.AlignCenter)
        mainLayout.addWidget(lblTableCaption)

        ### Buttons
        btnsLayout = qtw.QHBoxLayout()
        btnCrawlerRun = qtw.QPushButton('Run Crawler')
        btnCrawlerRun.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color : #ffd23f;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : #7a5d00;"
                                    "}"
                                    )
        btnCrawlerRun.setFont(qtg.QFont("Arial", 14))
        self.btnShowData = qtw.QPushButton('Show Data')
        self.btnShowData.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : #ffd23f;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : #7a5d00;"
                                       "}"
                                       )
        self.btnShowData.setFont(qtg.QFont("Arial", 14))
        self.btnShowData.setEnabled(True)
        # self.btnShowData.hide()

        btnsLayout.addWidget(btnCrawlerRun)
        btnsLayout.addWidget(self.btnShowData)
        mainLayout.addLayout(btnsLayout)

        ### Status
        ## will be hiddin on start
        statusLayout = qtw.QVBoxLayout()
        self.lblStatus = qtw.QLabel('Crawler Working...')
        self.lblStatus.hide()
        statusLayout.addWidget(self.lblStatus)
        mainLayout.addLayout(statusLayout)

        ### Actions on buttons click:
        # self.btnShowData.clicked.connect(lambda: self.show_data())
        self.btnShowData.clicked.connect(self.show_data)
        btnCrawlerRun.clicked.connect(self.run_crawler)

        # add spacer or just fixed spacing
        mainLayout.addSpacing(10)
        # mainLayout.addSpacerItem(qtw.QSpacerItem(0, 0, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding))

        mainWidget = qtw.QWidget()
        mainWidget.setLayout(mainLayout)

        self.setCentralWidget(mainWidget)

        self.show();

    def show_data(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.tableViewWidget = TableViewWidget(parent=self)
        self.tableViewWidget.show()

    def run_crawler(self):
        print('Crawler started')

        # change cursor to wait icon:
        self.setCursor(qtc.Qt.WaitCursor)

        # show status label
        self.lblStatus.show()
        qtw.QApplication.processEvents()  # needed to force processEvents

        # start crawler
        self.crawler = Crawler(MAIN_PAGE_PATH)
        self.crawler.run()

        # if crawler ready:
        if self.crawler.status:
            self.lblStatus.setText('Ready!')
            self.btnShowData.setEnabled(True)

        self.setCursor(qtc.Qt.ArrowCursor)


if __name__ == "__main__":
    # crawler = Crawler(BASE_URL)
    # crawler.run()

    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    sys.exit(app.exec_())