# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_dlsp.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1396, 974)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 20, 1141, 781))
        self.tabWidget.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.Grundansicht = QWidget()
        self.Grundansicht.setObjectName(u"Grundansicht")
        self.label_12 = QLabel(self.Grundansicht)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 1111, 71))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.114, y1:0.131, x2:1, y2:1, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(201, 216, 238, 255));")
        self.label_9 = QLabel(self.Grundansicht)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 350, 561, 351))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"image: url(:/gui_icons/Waschmaschine.png);")
        self.textBrowser = QTextBrowser(self.Grundansicht)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 110, 1111, 181))
        self.textBrowser.setFont(font1)
        self.textBrowser.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setLineWidth(1)
        self.label_56 = QLabel(self.Grundansicht)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 80, 171, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_56.setFont(font2)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_44 = QLabel(self.Grundansicht)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(740, 420, 91, 31))
        font3 = QFont()
        font3.setPointSize(16)
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_aus_Zustand_1 = QLabel(self.Grundansicht)
        self.LED_aus_Zustand_1.setObjectName(u"LED_aus_Zustand_1")
        self.LED_aus_Zustand_1.setGeometry(QRect(680, 420, 41, 31))
        self.LED_aus_Zustand_1.setFont(font1)
        self.LED_aus_Zustand_1.setStyleSheet(u"image: url(:/gui_icons/LED_aus.png);")
        self.LED_an_Zustand_2 = QLabel(self.Grundansicht)
        self.LED_an_Zustand_2.setObjectName(u"LED_an_Zustand_2")
        self.LED_an_Zustand_2.setGeometry(QRect(680, 510, 41, 31))
        self.LED_an_Zustand_2.setFont(font1)
        self.LED_an_Zustand_2.setStyleSheet(u"image: url(:/gui_icons/LED_an.png);")
        self.label_19 = QLabel(self.Grundansicht)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(740, 510, 91, 31))
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_aus_Zustand_3 = QLabel(self.Grundansicht)
        self.LED_aus_Zustand_3.setObjectName(u"LED_aus_Zustand_3")
        self.LED_aus_Zustand_3.setGeometry(QRect(680, 600, 41, 31))
        self.LED_aus_Zustand_3.setFont(font1)
        self.LED_aus_Zustand_3.setStyleSheet(u"image: url(:/gui_icons/LED_aus.png);")
        self.label_43 = QLabel(self.Grundansicht)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(740, 600, 111, 31))
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_aus_Zustand_2 = QLabel(self.Grundansicht)
        self.LED_aus_Zustand_2.setObjectName(u"LED_aus_Zustand_2")
        self.LED_aus_Zustand_2.setGeometry(QRect(680, 510, 41, 31))
        self.LED_aus_Zustand_2.setFont(font1)
        self.LED_aus_Zustand_2.setStyleSheet(u"image: url(:/gui_icons/LED_aus.png);")
        self.LED_an_Zustand_3 = QLabel(self.Grundansicht)
        self.LED_an_Zustand_3.setObjectName(u"LED_an_Zustand_3")
        self.LED_an_Zustand_3.setGeometry(QRect(680, 600, 41, 31))
        self.LED_an_Zustand_3.setFont(font1)
        self.LED_an_Zustand_3.setStyleSheet(u"image: url(:/gui_icons/LED_an.png);")
        self.LED_an_Zustand_1 = QLabel(self.Grundansicht)
        self.LED_an_Zustand_1.setObjectName(u"LED_an_Zustand_1")
        self.LED_an_Zustand_1.setGeometry(QRect(680, 420, 41, 31))
        self.LED_an_Zustand_1.setFont(font1)
        self.LED_an_Zustand_1.setStyleSheet(u"image: url(:/gui_icons/LED_an.png);")
        self.label_5 = QLabel(self.Grundansicht)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 310, 261, 31))
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.stop_button = QPushButton(self.Grundansicht)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(40, 620, 181, 51))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.stop_button.setFont(font5)
        self.stop_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.logo_fh_aachen = QLabel(self.Grundansicht)
        self.logo_fh_aachen.setObjectName(u"logo_fh_aachen")
        self.logo_fh_aachen.setGeometry(QRect(40, 680, 181, 121))
        self.logo_fh_aachen.setFont(font1)
        self.logo_fh_aachen.setStyleSheet(u"image: url(:/gui_icons/FH_Aachen_Logo.png);")
        self.label_11 = QLabel(self.Grundansicht)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(860, 731, 271, 20))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setKerning(True)
        font6.setStyleStrategy(QFont.NoAntialias)
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_18 = QLabel(self.Grundansicht)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1010, 10, 111, 71))
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(True)
        self.label_18.setFont(font7)
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(91, 108, 126);")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.Grundansicht, "")
        self.label_9.raise_()
        self.label_5.raise_()
        self.LED_aus_Zustand_2.raise_()
        self.label_56.raise_()
        self.label_12.raise_()
        self.textBrowser.raise_()
        self.label_44.raise_()
        self.LED_aus_Zustand_1.raise_()
        self.LED_an_Zustand_2.raise_()
        self.label_19.raise_()
        self.LED_aus_Zustand_3.raise_()
        self.label_43.raise_()
        self.LED_an_Zustand_3.raise_()
        self.LED_an_Zustand_1.raise_()
        self.stop_button.raise_()
        self.logo_fh_aachen.raise_()
        self.label_11.raise_()
        self.label_18.raise_()
        self.Detailansicht = QWidget()
        self.Detailansicht.setObjectName(u"Detailansicht")
        self.LED_aus_Zustand_21 = QLabel(self.Detailansicht)
        self.LED_aus_Zustand_21.setObjectName(u"LED_aus_Zustand_21")
        self.LED_aus_Zustand_21.setGeometry(QRect(310, 210, 41, 31))
        self.LED_aus_Zustand_21.setFont(font1)
        self.LED_aus_Zustand_21.setStyleSheet(u"image: url(:/gui_icons/LED_aus.png);")
        self.label_13 = QLabel(self.Detailansicht)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(860, 731, 271, 20))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setTextFormat(Qt.PlainText)
        self.LED_an_Zustand_21 = QLabel(self.Detailansicht)
        self.LED_an_Zustand_21.setObjectName(u"LED_an_Zustand_21")
        self.LED_an_Zustand_21.setGeometry(QRect(310, 210, 41, 31))
        self.LED_an_Zustand_21.setFont(font1)
        self.LED_an_Zustand_21.setStyleSheet(u"image: url(:/gui_icons/LED_an.png);")
        self.stop_button_2 = QPushButton(self.Detailansicht)
        self.stop_button_2.setObjectName(u"stop_button_2")
        self.stop_button_2.setGeometry(QRect(40, 620, 181, 51))
        self.stop_button_2.setFont(font5)
        self.stop_button_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.logo_fh_aachen_2 = QLabel(self.Detailansicht)
        self.logo_fh_aachen_2.setObjectName(u"logo_fh_aachen_2")
        self.logo_fh_aachen_2.setGeometry(QRect(40, 680, 181, 121))
        self.logo_fh_aachen_2.setFont(font1)
        self.logo_fh_aachen_2.setStyleSheet(u"image: url(:/gui_icons/FH_Aachen_Logo.png);")
        self.LED_an_Zustand_11 = QLabel(self.Detailansicht)
        self.LED_an_Zustand_11.setObjectName(u"LED_an_Zustand_11")
        self.LED_an_Zustand_11.setGeometry(QRect(310, 150, 41, 31))
        self.LED_an_Zustand_11.setFont(font1)
        self.LED_an_Zustand_11.setStyleSheet(u"image: url(:/gui_icons/LED_an.png);")
        self.label_10 = QLabel(self.Detailansicht)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 120, 421, 201))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"image: url(:/gui_icons/Waschmaschine.png);")
        self.LED_aus_Zustand_11 = QLabel(self.Detailansicht)
        self.LED_aus_Zustand_11.setObjectName(u"LED_aus_Zustand_11")
        self.LED_aus_Zustand_11.setGeometry(QRect(310, 150, 41, 31))
        self.LED_aus_Zustand_11.setFont(font1)
        self.LED_aus_Zustand_11.setStyleSheet(u"image: url(:/gui_icons/LED_aus.png);")
        self.LED_an_Zustand_31 = QLabel(self.Detailansicht)
        self.LED_an_Zustand_31.setObjectName(u"LED_an_Zustand_31")
        self.LED_an_Zustand_31.setGeometry(QRect(310, 270, 41, 31))
        self.LED_an_Zustand_31.setFont(font1)
        self.LED_an_Zustand_31.setStyleSheet(u"image: url(:/gui_icons/LED_an.png);")
        self.label_15 = QLabel(self.Detailansicht)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 1111, 71))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.114, y1:0.131, x2:1, y2:1, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(201, 216, 238, 255));")
        self.textBrowser_2 = QTextBrowser(self.Detailansicht)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(610, 110, 511, 211))
        self.textBrowser_2.setFont(font1)
        self.textBrowser_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_2.setLineWidth(1)
        self.label_21 = QLabel(self.Detailansicht)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(350, 210, 91, 31))
        font8 = QFont()
        font8.setPointSize(14)
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_aus_Zustand_31 = QLabel(self.Detailansicht)
        self.LED_aus_Zustand_31.setObjectName(u"LED_aus_Zustand_31")
        self.LED_aus_Zustand_31.setGeometry(QRect(310, 270, 41, 31))
        self.LED_aus_Zustand_31.setFont(font1)
        self.LED_aus_Zustand_31.setStyleSheet(u"image: url(:/gui_icons/LED_aus.png);")
        self.label_57 = QLabel(self.Detailansicht)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(610, 80, 171, 31))
        self.label_57.setFont(font2)
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_45 = QLabel(self.Detailansicht)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(350, 150, 81, 31))
        self.label_45.setFont(font8)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_46 = QLabel(self.Detailansicht)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(350, 270, 111, 31))
        self.label_46.setFont(font8)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.Detailansicht)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 80, 261, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.graphicsView = QChartView(self.Detailansicht)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(250, 340, 871, 391))
        self.graphicsView.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.114, y1:0.131, x2:1, y2:1, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(201, 216, 238, 255));")
        self.lcday = QLCDNumber(self.Detailansicht)
        self.lcday.setObjectName(u"lcday")
        self.lcday.setGeometry(QRect(150, 490, 51, 23))
        self.lcday.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.lcday.setSmallDecimalPoint(False)
        self.label_51 = QLabel(self.Detailansicht)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(50, 420, 181, 31))
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_48 = QLabel(self.Detailansicht)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(80, 520, 51, 21))
        self.label_48.setFont(font8)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_47 = QLabel(self.Detailansicht)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(80, 460, 51, 21))
        self.label_47.setFont(font8)
        self.label_47.setLayoutDirection(Qt.RightToLeft)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_47.setFrameShape(QFrame.NoFrame)
        self.label_47.setAlignment(Qt.AlignCenter)
        self.lcdax = QLCDNumber(self.Detailansicht)
        self.lcdax.setObjectName(u"lcdax")
        self.lcdax.setGeometry(QRect(150, 460, 51, 23))
        self.lcdax.setStyleSheet(u"")
        self.lcdax.setSmallDecimalPoint(False)
        self.label_49 = QLabel(self.Detailansicht)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(80, 490, 51, 21))
        self.label_49.setFont(font8)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_49.setAlignment(Qt.AlignCenter)
        self.lcdaz = QLCDNumber(self.Detailansicht)
        self.lcdaz.setObjectName(u"lcdaz")
        self.lcdaz.setGeometry(QRect(150, 520, 51, 23))
        self.lcdaz.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.lcdaz.setSmallDecimalPoint(False)
        self.label_22 = QLabel(self.Detailansicht)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(1010, 10, 111, 71))
        self.label_22.setFont(font7)
        self.label_22.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(91, 108, 126);")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.Detailansicht, "")
        self.label_10.raise_()
        self.label_45.raise_()
        self.label_6.raise_()
        self.label_57.raise_()
        self.LED_aus_Zustand_11.raise_()
        self.LED_aus_Zustand_31.raise_()
        self.LED_aus_Zustand_21.raise_()
        self.label_13.raise_()
        self.LED_an_Zustand_21.raise_()
        self.stop_button_2.raise_()
        self.logo_fh_aachen_2.raise_()
        self.LED_an_Zustand_11.raise_()
        self.LED_an_Zustand_31.raise_()
        self.label_15.raise_()
        self.textBrowser_2.raise_()
        self.label_21.raise_()
        self.label_46.raise_()
        self.graphicsView.raise_()
        self.lcday.raise_()
        self.label_51.raise_()
        self.label_48.raise_()
        self.label_47.raise_()
        self.lcdax.raise_()
        self.label_49.raise_()
        self.lcdaz.raise_()
        self.label_22.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1396, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Datenmanagement & Leittechnik - Wintersemester 2021/2022 \n"
"Projekt: Klassifizierung von Beschleunigungsdaten einer Waschmaschine", None))
        self.label_9.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Dialogfenster", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Stillstand", None))
        self.LED_aus_Zustand_1.setText("")
        self.LED_an_Zustand_2.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Waschen", None))
        self.LED_aus_Zustand_3.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Schleudern", None))
        self.LED_aus_Zustand_2.setText("")
        self.LED_an_Zustand_3.setText("")
        self.LED_an_Zustand_1.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Aktueller Waschstatus", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Programmstop", None))
        self.logo_fh_aachen.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Simon R\u00f6hser 3291574 & Magnus Diepers 3307011", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Basisansicht", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Grundansicht), QCoreApplication.translate("MainWindow", u"Grundansicht", None))
        self.LED_aus_Zustand_21.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Simon R\u00f6hser 3291574 & Magnus Diepers 3307011", None))
        self.LED_an_Zustand_21.setText("")
        self.stop_button_2.setText(QCoreApplication.translate("MainWindow", u"Programmstop", None))
        self.logo_fh_aachen_2.setText("")
        self.LED_an_Zustand_11.setText("")
        self.label_10.setText("")
        self.LED_aus_Zustand_11.setText("")
        self.LED_an_Zustand_31.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Datenmanagement & Leittechnik - Wintersemester 2021/2022 \n"
"Projekt: Klassifizierung von Beschleunigungsdaten einer Waschmaschine", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Waschen", None))
        self.LED_aus_Zustand_31.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Dialogfenster", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Stillstand", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Schleudern", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Aktueller Waschstatus", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Aktuelle Messwerte", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Az", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ax", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Ay", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Detailansicht", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Detailansicht), QCoreApplication.translate("MainWindow", u"Detailansicht", None))
    # retranslateUi

