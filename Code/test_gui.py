##################################################################################
# Import of the required libraries and files #####################################
##################################################################################
import pandas as pd
from pymongo import MongoClient
import time
import pandas as pd
from PySide6 import QtCharts
import time
from time import sleep
import numpy as np
from bson.json_util import dumps
from bson.json_util import loads
from datetime import datetime
from PySide6.QtGui import Qt
import gui_dlsp
import Icons
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import PySide6
from PySide6 import QtCharts
import sys
import matplotlib.pyplot as plt
import threading

##################################################################################
# Declaration of variables #######################################################
##################################################################################
time_data = []
accel_x = []
accel_y = []
accel_z = []

##################################################################################
# Define useful functions for the following program ##############################
##################################################################################
def data_refresh(collection, frequency):
    time_data.clear()
    accel_x.clear()
    accel_y.clear()
    accel_z.clear()
    data = collection.find()
    list_data = list(data)
    if len(list_data) > 500:
        list_data = list_data[len(list_data)-500:]
    df_data = pd.DataFrame(list_data)
    length_df_data = len(df_data)
    time_relation = df_data["time"][0]
    for i in range(length_df_data):
        time_list = df_data["time"][i]
        time_scaled = (int(time_list[2]) - int(time_relation[2])) * 24 * 60 * 60 + (int(time_list[3]) - int(time_relation[3])) * 60 * 60 + (int(time_list[4]) - int(time_relation[4])) * 60 + (int(time_list[5]) - int(time_relation[5])) + (int(time_list[6]) - int(time_relation[6])) / 1000
        time_data.append(time_scaled)
        accel = df_data["Accel"][i]
        accel_x.append(float(accel[0]))
        accel_y.append(float(accel[1]))
        accel_z.append(float(accel[2]))
    df_data.insert(3, "Timestamp", time_data)
    df_data.insert(4, "Ax", accel_x)
    df_data.insert(5, "Ay", accel_y)
    df_data.insert(6, "Az", accel_z)
    del df_data["_id"]
    del df_data["Accel"]
    del df_data["time"]
    freq_ax = calcFFT(accel_x, length_df_data)
    freq_ay = calcFFT(accel_y, length_df_data)
    freq_az = calcFFT(accel_z, length_df_data)
    x_freq = np.linspace(0.0, frequency / 2.0, int(length_df_data / 2) + 1)
    y_freq = np.linspace(0.0, frequency / 2.0, int(length_df_data / 2) + 1)
    z_freq = np.linspace(0.0, frequency / 2.0, int(length_df_data / 2) + 1)
    return df_data, freq_ax, freq_ay, freq_az, x_freq, y_freq, z_freq

def calcFFT(accel,nrsamples):
    accel_without_mean = accel - np.mean(accel)  # Subtract mean Value to reduce the DC Offset in the FFT
    freq = np.fft.rfft(accel_without_mean, nrsamples, norm='ortho')
    freq = np.abs(freq)
    freq = freq / nrsamples  # Normalize the Amplitude by the known sample number
    return freq

##################################################################################
# Initialization and program of the gui ##########################################
##################################################################################
class Window(QMainWindow, gui_dlsp.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.textBrowser.insertPlainText("GUI wurde gestartet...\n\n")

        self.acce_series_ax = QtCharts.QLineSeries()
        self.acce_series_ax.setName("Accel_x")
        self.acce_series_ay = QtCharts.QLineSeries()
        self.acce_series_ay.setName("Accel_y")
        self.acce_series_az = QtCharts.QLineSeries()
        self.acce_series_az.setName("Accel_z")
        self.acce_series_az = QtCharts.QLineSeries()

        self.acce_chart = QtCharts.QChart()
        self.acce_chart.addSeries(self.acce_series_ax)
        self.acce_chart.addSeries(self.acce_series_ay)
        self.acce_chart.addSeries(self.acce_series_az)
        self.acce_chart.legend().setAlignment(Qt.AlignRight)
        self.acce_chart.createDefaultAxes()

        self.acce_chart.axisX().setTitleText('Time [s]')
        self.acce_chart.axisY().setTitleText('Acceleration [m/s²]')

        self.graphicsView.setLineWidth(0.5)
        self.acce_chart.setTheme(PySide6.QtCharts.QChart.ChartThemeBlueIcy)

        led_reset(self)


    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
                )

def update_chart(win, collection):
    frequency = win.spinBox.value()
    win.acce_series_ax.clear()
    win.acce_series_ay.clear()
    win.acce_series_az.clear()
    df_data, freq_ax, freq_ay, freq_az, x_freq, y_freq, z_freq = data_refresh(collection, frequency)
    accel_x = df_data["Ax"]
    accel_y = df_data["Ay"]
    accel_z = df_data["Az"]
    time_data = df_data["Timestamp"]
    if win.comboBox.currentText() == "Bitte Auswertungsart auswählen":
        win.textBrowser.insertPlainText("Bitte wählen Sie Ihre gewünschte Auswertungsart\n\n")
    elif win.comboBox.currentText() == "Beschleunigung":
        win.graphicsView.setChart(win.acce_chart)
        if abs(min(min(accel_x), min(accel_y), min(accel_z))) > abs(max(max(accel_x), max(accel_y), max(accel_z))):
            range_min = min(min(accel_x), min(accel_y), min(accel_z)) - 0.15
            range_max = range_min * (-1)
        else:
            range_max = max(max(accel_x), max(accel_y), max(accel_z)) + 0.15
            range_min = range_max * (-1)
        for i in range(500):
            win.acce_series_ax.append(time_data[i], accel_x[i])
            win.acce_series_ay.append(time_data[i], accel_y[i])
            win.acce_series_az.append(time_data[i], accel_z[i])
        win.acce_chart.axisX().setRange(min(time_data), max(time_data))
        win.acce_chart.axisY().setRange(range_min, range_max)
    elif win.comboBox.currentText() == "Beschleunigung & Frequenz":
        win.graphicsView.setChart(win.acce_freq_chart)
    elif win.comboBox.currentText() == "X-Achse":
        win.graphicsView.setChart(win.x_chart)
    elif win.comboBox.currentText() == "Y-Achse":
        win.graphicsView.setChart(win.y_chart)
    elif win.comboBox.currentText() == "Z-Achse":
        win.graphicsView.setChart(win.z_chart)

    win.lcdax.display(accel_x[499])
    win.lcday.display(accel_y[499])
    win.lcdaz.display(accel_z[499])

    fttfig, (ax1, ax2) = plt.subplots(2, figsize=(5, 5))

    if win.comboBox.currentText() == 'Bitte Auswertungsart auswählen':
        ax1.plot(time_data, accel_x, '.-', label="Accel_Ax", linewidth=0.5, ms=1)
        ax1.plot(time_data, accel_y, '.-', label="Accel_Ay", linewidth=0.5, ms=1)
        ax1.plot(time_data, accel_z, '.-', label="Accel_Az", linewidth=0.5, ms=1)

        ax2.plot(x_freq, freq_ax, '.-', label="ax_freq", linewidth=0.5, ms=1)
        ax2.plot(x_freq, freq_ay, '.-', label="ay_freq", linewidth=0.5, ms=1)
        ax2.plot(x_freq, freq_az, '.-', label="az_freq", linewidth=0.5, ms=1)

    elif win.comboBox.currentText() == 'Beschleunigung':
        ax1.plot(time_data, accel_x, '.-', label="Accel_Ax", linewidth=0.5, ms=1)
        ax1.plot(time_data, accel_y, '.-', label="Accel_Ay", linewidth=0.5, ms=1)
        ax1.plot(time_data, accel_z, '.-', label="Accel_Az", linewidth=0.5, ms=1)

    elif win.comboBox.currentText() == 'Beschleunigung & Frequenz':
        ax1.plot(time_data, accel_x, '.-', label="Accel_Ax", linewidth=0.5, ms=1)
        ax1.plot(time_data, accel_y, '.-', label="Accel_Ay", linewidth=0.5, ms=1)
        ax1.plot(time_data, accel_z, '.-', label="Accel_Az", linewidth=0.5, ms=1)

        ax2.plot(x_freq, freq_ax, '.-', label="ax_freq", linewidth=0.5, ms=1)
        ax2.plot(x_freq, freq_ay, '.-', label="ay_freq", linewidth=0.5, ms=1)
        ax2.plot(x_freq, freq_az, '.-', label="az_freq", linewidth=0.5, ms=1)

    elif win.comboBox.currentText() == 'X-Achse':
        ax1.plot(time_data, accel_x, '.-', label="Accel_Ax", linewidth=0.5, ms=1)

        ax2.plot(x_freq, freq_ax, '.-', label="ax_freq", linewidth=0.5, ms=1)

    elif win.comboBox.currentText() == 'Achse Y':
        ax1.plot(time_data, accel_y, '.-', label="Accel_Ay", linewidth=0.5, ms=1)

        ax2.plot(x_freq, freq_ay, '.-', label="ay_freq", linewidth=0.5, ms=1)

    elif win.comboBox.currentText() == 'Achse Z':
        ax1.plot(time_data, accel_z, '.-', label="Accel_Az", linewidth=0.5, ms=1)

        ax2.plot(x_freq, freq_az, '.-', label="az_freq", linewidth=0.5, ms=1)

    ax1.set_title("IMU history from MongoDB")
    ax1.set(xlabel="Time [s]")
    ax1.set(ylabel="Acceleration [m/s²]")
    ax1.legend()
    ax1.grid(True)

    ax2.set(xlabel="Frequency [Hz]")
    ax2.set(ylabel="Amplitude")
    ax2.legend()
    ax2.grid(True)
    plt.show()


def led_reset(self):
    self.LED_maschinelles_lernen.setEnabled(False)
    self.LED_maschinelles_lernen.setStyleSheet(u"background-color: rgb(91, 108, 126);")
    self.LED_maschinelles_lernen_2.setEnabled(False)
    self.LED_maschinelles_lernen_2.setStyleSheet(u"background-color: rgb(91, 108, 126);")
    self.LED_maschinelles_lernen_3.setEnabled(False)
    self.LED_maschinelles_lernen_3.setStyleSheet(u"background-color: rgb(91, 108, 126);")
    self.LED_maschinelles_lernen_4.setEnabled(False)
    self.LED_maschinelles_lernen_4.setStyleSheet(u"background-color: rgb(91, 108, 126);")
    self.LED_spuelen.setEnabled(False)
    self.LED_spuelen.setStyleSheet(u"background-color: rgb(56, 56, 56);")
    self.LED_waschen.setEnabled(False)
    self.LED_waschen.setStyleSheet(u"background-color: rgb(56, 56, 56);")
    self.LED_schleudern.setEnabled(False)
    self.LED_schleudern.setStyleSheet(u"background-color: rgb(56, 56, 56);")
    self.LED_schleudern_2.setEnabled(False)
    self.LED_schleudern_2.setStyleSheet(u"background-color: rgb(56, 56, 56);")
    self.LED_schleudern_3.setEnabled(False)
    self.LED_schleudern_3.setStyleSheet(u"background-color: rgb(56, 56, 56);")

def machine_learning(collection_train_data_ml):
    print("Hier sollte das Machine Learning stattfinden")
##################################################################################
# Connection to Mongo DB #########################################################
##################################################################################
client = MongoClient("localhost:27017")
db = client.DLSP
collection = db.Test
collection_train_data_ml = db.Machine_Learning

while True:
    app = QApplication(sys.argv)
    win = Window()
    update_chart(win, collection)
    win.showMaximized()
    sys.exit(app.exec())
    time.sleep(1)
collection.close()
print("Connection to MongoDB terminated")