import PySide6.QtCharts
import pandas as pd
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCharts
import time
from time import time
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads

from datetime import datetime
from time import localtime, sleep

from PySide6.QtGui import Qt
import gui_dlsp
import Icons
from PySide6.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox)
import PySide6
from PySide6 import QtCharts
import sys
import matplotlib.pyplot as plt
import threading

class Window(QMainWindow, gui_dlsp.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.acce_series_ax = QtCharts.QLineSeries()
        self.acce_series_ax.setName(" a_x")

        self.acce_series_ay = QtCharts.QLineSeries()
        self.acce_series_ay.setName(" a_y")

        self.acce_series_az = QtCharts.QLineSeries()
        self.acce_series_az.setName(" a_z")

        self.acce_chart = QtCharts.QChart()
        self.acce_chart.addSeries(self.acce_series_ax)
        self.acce_chart.addSeries(self.acce_series_ay)
        self.acce_chart.addSeries(self.acce_series_az)
        self.acce_chart.legend().setAlignment(Qt.AlignRight)
        self.acce_chart.createDefaultAxes()

        self.acce_chart.axisX().setTitleText('Time')
        self.acce_chart.axisY().setTitleText('Acceleration')

        self.graphicsView.setLineWidth(0.5)
        self.graphicsView.setChart(self.acce_chart)
        self.acce_chart.setTheme(PySide6.QtCharts.QChart.ChartThemeBlueIcy)

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

    def led_reset(self):
        self.LED_maschinelles_lernen.setEnabled(False)
        self.LED_maschinelles_lernen_2.setEnabled(False)
        self.LED_maschinelles_lernen_3.setEnabled(False)
        self.LED_maschinelles_lernen_4.setEnabled(False)
        self.LED_spuelen.setEnabled(False)
        self.LED_waschen.setEnabled(False)
        self.LED_schleudern.setEnabled(False)
        self.LED_schleudern_2.setEnabled(False)
        self.LED_schleudern_3.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.led_reset()
    win.showMaximized()
    sys.exit(app.exec())