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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLCDNumber,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1396, 901)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1401, 881))
        self.frame.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.graphicsView = QChartView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(280, 380, 1081, 471))
        self.graphicsView.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.114, y1:0.131, x2:1, y2:1, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(201, 216, 238, 255));")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 350, 171, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 360, 181, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(450, 350, 171, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1090, 850, 271, 31))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 10, 1331, 71))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.114, y1:0.131, x2:1, y2:1, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(201, 216, 238, 255));")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 440, 241, 31))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 470, 171, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_waschen = QLabel(self.frame)
        self.LED_waschen.setObjectName(u"LED_waschen")
        self.LED_waschen.setGeometry(QRect(40, 470, 31, 31))
        self.LED_waschen.setFont(font3)
        self.LED_waschen.setStyleSheet(u"image: url(:/Icons/LED_blau.png);")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(90, 550, 181, 31))
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(90, 510, 171, 31))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(30, 390, 61, 22))
        self.spinBox.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.spinBox.setMinimum(60)
        self.spinBox.setMaximum(200)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 90, 1331, 251))
        self.frame_2.setStyleSheet(u"background-color: rgb(91, 108, 126);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 241, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(91, 108, 126);")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 50, 151, 21))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"background-color: rgb(91, 108, 126);\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 50, 121, 21))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(91, 108, 126);")
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(430, 50, 91, 21))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(91, 108, 126);\n"
"")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(420, 100, 111, 81))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"image: url(:/Icons/Waschmaschine.png);\n"
"background-color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(210, 80, 121, 111))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"image: url(:/Icons/mqtt-logo.png);")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 131, 91))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"image: url(:/Icons/maschinelles_Lernen.png);")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 110, 51, 51))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"image: url(:/Icons/Pfeil.png);")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 110, 51, 51))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"image: url(:/Icons/Pfeil.png);")
        self.LED_maschinelles_lernen = QLabel(self.frame_2)
        self.LED_maschinelles_lernen.setObjectName(u"LED_maschinelles_lernen")
        self.LED_maschinelles_lernen.setGeometry(QRect(60, 190, 41, 31))
        self.LED_maschinelles_lernen.setFont(font3)
        self.LED_maschinelles_lernen.setStyleSheet(u"image: url(:/Icons/LED_gruen.png);")
        self.label_53 = QLabel(self.frame_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(610, 100, 111, 81))
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"image: url(:/Icons/Messung.png);\n"
"background-color: rgb(255, 255, 255);")
        self.label_54 = QLabel(self.frame_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(550, 110, 51, 51))
        self.label_54.setFont(font3)
        self.label_54.setStyleSheet(u"image: url(:/Icons/Pfeil.png);")
        self.label_55 = QLabel(self.frame_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(620, 50, 91, 21))
        self.label_55.setFont(font3)
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(91, 108, 126);\n"
"")
        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(740, 30, 571, 211))
        self.textBrowser.setFont(font3)
        self.textBrowser.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setLineWidth(1)
        self.label_56 = QLabel(self.frame_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(740, 10, 201, 21))
        self.label_56.setFont(font3)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(91, 108, 126);\n"
"")
        self.LED_maschinelles_lernen_2 = QLabel(self.frame_2)
        self.LED_maschinelles_lernen_2.setObjectName(u"LED_maschinelles_lernen_2")
        self.LED_maschinelles_lernen_2.setGeometry(QRect(260, 190, 41, 31))
        self.LED_maschinelles_lernen_2.setFont(font3)
        self.LED_maschinelles_lernen_2.setStyleSheet(u"image: url(:/Icons/LED_gruen.png);")
        self.LED_maschinelles_lernen_3 = QLabel(self.frame_2)
        self.LED_maschinelles_lernen_3.setObjectName(u"LED_maschinelles_lernen_3")
        self.LED_maschinelles_lernen_3.setGeometry(QRect(460, 190, 41, 31))
        self.LED_maschinelles_lernen_3.setFont(font3)
        self.LED_maschinelles_lernen_3.setStyleSheet(u"image: url(:/Icons/LED_gruen.png);")
        self.LED_maschinelles_lernen_4 = QLabel(self.frame_2)
        self.LED_maschinelles_lernen_4.setObjectName(u"LED_maschinelles_lernen_4")
        self.LED_maschinelles_lernen_4.setGeometry(QRect(650, 190, 41, 31))
        self.LED_maschinelles_lernen_4.setFont(font3)
        self.LED_maschinelles_lernen_4.setStyleSheet(u"image: url(:/Icons/LED_gruen.png);")
        self.LED_spuelen = QLabel(self.frame)
        self.LED_spuelen.setObjectName(u"LED_spuelen")
        self.LED_spuelen.setGeometry(QRect(40, 510, 31, 31))
        self.LED_spuelen.setFont(font3)
        self.LED_spuelen.setStyleSheet(u"image: url(:/Icons/LED_blau.png);")
        self.LED_schleudern = QLabel(self.frame)
        self.LED_schleudern.setObjectName(u"LED_schleudern")
        self.LED_schleudern.setGeometry(QRect(40, 550, 31, 31))
        self.LED_schleudern.setFont(font3)
        self.LED_schleudern.setStyleSheet(u"image: url(:/Icons/LED_blau.png);")
        self.lcdax = QLCDNumber(self.frame)
        self.lcdax.setObjectName(u"lcdax")
        self.lcdax.setGeometry(QRect(30, 730, 51, 23))
        self.lcdax.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.lcdax.setSmallDecimalPoint(False)
        self.lcday = QLCDNumber(self.frame)
        self.lcday.setObjectName(u"lcday")
        self.lcday.setGeometry(QRect(90, 730, 51, 23))
        self.lcday.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.lcday.setSmallDecimalPoint(False)
        self.lcdaz = QLCDNumber(self.frame)
        self.lcdaz.setObjectName(u"lcdaz")
        self.lcdaz.setGeometry(QRect(150, 730, 51, 23))
        self.lcdaz.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.lcdaz.setSmallDecimalPoint(False)
        self.label_46 = QLabel(self.frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(30, 710, 51, 21))
        self.label_46.setFont(font3)
        self.label_46.setLayoutDirection(Qt.RightToLeft)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_46.setFrameShape(QFrame.NoFrame)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_47 = QLabel(self.frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(90, 710, 51, 21))
        self.label_47.setFont(font3)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_47.setAlignment(Qt.AlignCenter)
        self.label_48 = QLabel(self.frame)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(150, 710, 51, 21))
        self.label_48.setFont(font3)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_51 = QLabel(self.frame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(30, 680, 191, 31))
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_schleudern_2 = QLabel(self.frame)
        self.LED_schleudern_2.setObjectName(u"LED_schleudern_2")
        self.LED_schleudern_2.setGeometry(QRect(40, 590, 31, 31))
        self.LED_schleudern_2.setFont(font3)
        self.LED_schleudern_2.setStyleSheet(u"image: url(:/Icons/LED_blau.png);")
        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(90, 590, 181, 31))
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LED_schleudern_3 = QLabel(self.frame)
        self.LED_schleudern_3.setObjectName(u"LED_schleudern_3")
        self.LED_schleudern_3.setGeometry(QRect(40, 630, 31, 31))
        self.LED_schleudern_3.setFont(font3)
        self.LED_schleudern_3.setStyleSheet(u"image: url(:/Icons/LED_blau.png);")
        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(90, 630, 181, 31))
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 390, 121, 24))
        self.pushButton.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.logo_fh_aachen = QLabel(self.frame)
        self.logo_fh_aachen.setObjectName(u"logo_fh_aachen")
        self.logo_fh_aachen.setGeometry(QRect(0, 810, 231, 121))
        self.logo_fh_aachen.setFont(font3)
        self.logo_fh_aachen.setStyleSheet(u"image: url(:/Icons/FH_Aachen_Logo.png);")
        self.label_49 = QLabel(self.frame)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(80, 760, 71, 21))
        self.label_49.setFont(font3)
        self.label_49.setLayoutDirection(Qt.RightToLeft)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_49.setFrameShape(QFrame.NoFrame)
        self.label_49.setAlignment(Qt.AlignCenter)
        self.lcdax_2 = QLCDNumber(self.frame)
        self.lcdax_2.setObjectName(u"lcdax_2")
        self.lcdax_2.setGeometry(QRect(90, 780, 51, 23))
        self.lcdax_2.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.lcdax_2.setSmallDecimalPoint(False)
        self.label_2.raise_()
        self.label.raise_()
        self.label_11.raise_()
        self.frame_2.raise_()
        self.graphicsView.raise_()
        self.comboBox.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.LED_waschen.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.spinBox.raise_()
        self.LED_spuelen.raise_()
        self.LED_schleudern.raise_()
        self.lcdax.raise_()
        self.lcday.raise_()
        self.lcdaz.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.label_51.raise_()
        self.LED_schleudern_2.raise_()
        self.label_43.raise_()
        self.LED_schleudern_3.raise_()
        self.label_44.raise_()
        self.pushButton.raise_()
        self.logo_fh_aachen.raise_()
        self.label_49.raise_()
        self.lcdax_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1396, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datenauswertung", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Abtastfrequenz [Hz]", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bitte Auswertungsart ausw\u00e4hlen", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Beschleunigung", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Beschleunigung & Frequenz", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Simon R\u00f6hser 3291574 & Magnus Diepers 3307011", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Datenmanagement & Leittechnik - Wintersemester 2021/2022 \n"
"Projekt: Klassifizierung von Beschleunigungsdaten einer Waschmaschine", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Aktuelles Waschprogramm", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Stillstand", None))
        self.LED_waschen.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Waschen", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Vorw\u00e4sche", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Aktueller Programmstatus", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Maschinelles Lernen", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Frequenzabfrage", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Messung", None))
        self.label_9.setText("")
        self.label_21.setText("")
        self.label_4.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.LED_maschinelles_lernen.setText("")
        self.label_53.setText("")
        self.label_54.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Verarbeitung", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Dialogfenster", None))
        self.LED_maschinelles_lernen_2.setText("")
        self.LED_maschinelles_lernen_3.setText("")
        self.LED_maschinelles_lernen_4.setText("")
        self.LED_spuelen.setText("")
        self.LED_schleudern.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Ax", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ay", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Az", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Aktuelle Messwerte", None))
        self.LED_schleudern_2.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Schleudern", None))
        self.LED_schleudern_3.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Sp\u00fclen", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u00c4nderung best\u00e4tigen", None))
        self.logo_fh_aachen.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Agesamt", None))
    # retranslateUi

