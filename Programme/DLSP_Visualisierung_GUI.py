########################################################################################################################
# Import of the required libraries and files                                                                           #
########################################################################################################################
from pymongo import MongoClient
import pandas as pd
from PySide6 import QtCharts
from time import sleep, localtime
import numpy as np
from PySide6.QtGui import Qt, QColor
import gui_dlsp as gui
import Icons
from PySide6.QtWidgets import QApplication, QMainWindow
import PySide6
from PySide6 import QtCharts
import sys
import threading
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

########################################################################################################################
# Declaration of variables                                                                                             #
########################################################################################################################
time_data = []
accel_x = []
accel_y = []
accel_z = []
start_time = localtime()[:6]

########################################################################################################################
# Define useful functions for the following program                                                                    #
########################################################################################################################


def data_refresh(collection):
    time_data.clear()
    accel_x.clear()
    accel_y.clear()
    accel_z.clear()
    list_data = list(collection.find())
    if len(list_data) > 250:
        list_data = list_data[len(list_data) - 250:]
    df_data = pd.DataFrame(list_data)
    for i in range(len(df_data)):
        time_scaled = (int(df_data["time"][i][2]) - int(start_time[2])) * 24 * 60 * 60 + (
                    int(df_data["time"][i][3]) + 1 - int(start_time[3])) * 60 * 60 + (
                                  int(df_data["time"][i][4]) - int(start_time[4])) * 60 + (
                                  int(df_data["time"][i][5]) - int(start_time[5])) + (
                                  int(df_data["time"][i][6]) - 0) / 1000
        if time_scaled >= 0:
            time_scaled = round(time_scaled, 3)
            time_data.append(time_scaled)
            accel_x.append(float(df_data["Ax"][i]))
            accel_y.append(float(df_data["Ay"][i]))
            accel_z.append(float(df_data["Az"][i]))
    df_new_data = pd.DataFrame({"Timestamp": time_data, "Ax": accel_x, "Ay": accel_y, "Az": accel_z})
    return df_new_data


def ext_data_refresh(collection):
    df_ext_data = pd.DataFrame(list(collection.find()))
    return df_ext_data


def calcFFT(accel, nrsamples):
    accel_without_mean = accel - np.mean(accel)  # Subtract mean Value to reduce the DC Offset in the FFT
    freq = np.fft.rfft(accel_without_mean, nrsamples, norm='ortho')
    freq = np.abs(freq)
    freq = freq / nrsamples  # Normalize the Amplitude by the known sample number
    return freq


def gen_test_data(df):
    StartSample = 0
    LengthSample = len(df.index)
    EndSample = StartSample+LengthSample

    a_x = df.iloc[StartSample:EndSample, 0].values
    a_y = df.iloc[StartSample:EndSample, 1].values
    a_z = df.iloc[StartSample:EndSample, 2].values

    a_abs = np.sqrt(a_x*a_x+a_y*a_y+a_z*a_z)

    fs = 100.0  # Sample Frequency 100 Hz
    SampleNr = LengthSample
    Period = 1/fs

    x_time = np.linspace(0.0, Period*SampleNr, SampleNr)
    x_freq = np.linspace(0.0, fs/2.0, int(SampleNr/2)+1)

    aabs_freq = calcFFT(a_abs, SampleNr)
    return aabs_freq, x_time, x_freq


def external_chart():
    frequency = 10
    ax = []
    ay = []
    az = []
    df_ext_data = ext_data_refresh(collection)
    length_ext_vis = len(df_ext_data)
    df_ext_data = df_ext_data[length_ext_vis - 2000:]
    for i in df_ext_data.index:
        ax.append(float(df_ext_data["Ax"][i]))
        ay.append(float(df_ext_data["Ay"][i]))
        az.append(float(df_ext_data["Az"][i]))
    freq_ax = calcFFT(ax, length_ext_vis)
    freq_ay = calcFFT(ay, length_ext_vis)
    freq_az = calcFFT(az, length_ext_vis)
    x_freq = np.linspace(0.0, frequency / 2.0, int(length_ext_vis / 2) + 1)
    y_freq = np.linspace(0.0, frequency / 2.0, int(length_ext_vis / 2) + 1)
    z_freq = np.linspace(0.0, frequency / 2.0, int(length_ext_vis / 2) + 1)

    fttfig, (ax1, ax2) = plt.subplots(2, figsize=(15, 15))

    ax1.plot(df_ext_data.index, df_ext_data["Ax"], '.-', label="Accel_Ax", linewidth=0.5, ms=1, color="navy")
    ax1.plot(df_ext_data.index, df_ext_data["Ay"], '.-', label="Accel_Ay", linewidth=0.5, ms=1, color="royalblue")
    ax1.plot(df_ext_data.index, df_ext_data["Az"], '.-', label="Accel_Az", linewidth=0.5, ms=1, color="deepskyblue")

    ax2.plot(x_freq, freq_ax, '.-', label="ax_freq", linewidth=0.5, ms=1, color="navy")
    ax2.plot(y_freq, freq_ay, '.-', label="ay_freq", linewidth=0.5, ms=1, color="royalblue")
    ax2.plot(z_freq, freq_az, '.-', label="az_freq", linewidth=0.5, ms=1, color="deepskyblue")

    ax1.set_title("Data visualization of the last 2.000 collected data records")
    ax1.set(xlabel="Data record [#]")
    ax1.set(ylabel="Acceleration [m/s²]")
    ax1.legend()
    ax1.grid(True)

    ax2.set(xlabel="Frequency [Hz]")
    ax2.set(ylabel="Amplitude")
    ax2.legend()
    ax2.grid(True)
    plt.show()

########################################################################################################################
# Initialization and program of the gui                                                                                #
########################################################################################################################


class Window(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.textBrowser.insertPlainText("GUI wurde gestartet...\n\n")
        self.textBrowser_2.insertPlainText("GUI wurde gestartet...\n\n")

        self.acce_series_ax = QtCharts.QLineSeries()
        self.acce_series_ax.setName("Accel_x")
        self.acce_series_ay = QtCharts.QLineSeries()
        self.acce_series_ay.setName("Accel_y")
        self.acce_series_az = QtCharts.QLineSeries()
        self.acce_series_az.setName("Accel_z")

        self.acce_chart = QtCharts.QChart()
        self.acce_chart.addSeries(self.acce_series_ax)
        self.acce_chart.addSeries(self.acce_series_ay)
        self.acce_chart.addSeries(self.acce_series_az)
        self.acce_chart.legend().setAlignment(Qt.AlignRight)
        self.acce_chart.createDefaultAxes()
        self.acce_chart.axisX().setTitleText('Time [s]')
        self.acce_chart.axisY().setTitleText('Acceleration [m/s²]')
        self.acce_chart.setTheme(PySide6.QtCharts.QChart.ChartThemeDark)
        self.acce_series_ax.setColor(QColor(255, 255, 255))
        self.acce_series_ay.setColor(QColor(184, 227, 255))
        self.acce_series_az.setColor(QColor(193, 193, 255))

        self.graphicsView.setLineWidth(0.5)
        self.graphicsView.setChart(self.acce_chart)

        self.LED_states(led_state=0)

        self.stop_button.setCheckable(True)
        self.stop_button_2.setCheckable(True)

    def text_block(self, text_string):
        current_time = localtime()[3:6]
        text_print = str(current_time[0]) + ":" + str(current_time[1]) + ":" + str(current_time[2]) + "   " + text_string
        return text_print

    def both_dialogues(self, text_string):
        text_print = self.text_block(text_string)
        self.textBrowser.insertPlainText(text_print)
        self.textBrowser_2.insertPlainText(text_print)

    def update_chart(self):
        client = MongoClient("localhost:27017")
        db = client.DLSP
        collection = db.Test
        sc, classifier = self.machine_learning_training()
        while True:
            df_new_data = data_refresh(collection)
            if len(df_new_data) > 0:
                accel_x = df_new_data["Ax"]
                accel_y = df_new_data["Ay"]
                accel_z = df_new_data["Az"]
                time_data = df_new_data["Timestamp"]
                if max(abs(min(accel_x)), abs(min(accel_y)), abs(min(accel_z)), max(accel_x), max(accel_y), max(accel_z)) > 1.9:
                    range_max = max(abs(min(accel_x)), abs(min(accel_y)), abs(min(accel_z)), max(accel_x), max(accel_y), max(accel_z))
                    range_min = range_max * (-1)
                    self.textBrowser.setTextColor(QColor(255, 0, 0))
                    self.textBrowser_2.insertPlainText(self.text_block("Achtung angepasste Diagrammgrenzen!\n Ymin: " + str(range_min) + "Ymax: " + str(range_max) + "\n"))
                    self.textBrowser.setTextColor(QColor(255, 255, 255))
                else:
                    range_max = 2
                    range_min = -2
                self.acce_series_ax.clear()
                self.acce_series_ay.clear()
                self.acce_series_az.clear()
                for i in range(len(df_new_data)-1):
                    self.acce_series_ax.append(time_data[i], accel_x[i])
                    self.acce_series_ay.append(time_data[i], accel_y[i])
                    self.acce_series_az.append(time_data[i], accel_z[i])
                self.acce_chart.axisX().setRange(min(time_data), max(time_data))
                self.acce_chart.axisY().setRange(range_min, range_max)

                self.lcdax.display(accel_x[len(df_new_data)-1])
                self.lcday.display(accel_y[len(df_new_data)-1])
                self.lcdaz.display(accel_z[len(df_new_data)-1])

                self.machine_learning_classification(sc, classifier, df_new_data)

            else:
                self.textBrowser_2.insertPlainText(self.text_block("Warte auf Diagrammdaten...\n"))
                sleep(5)

            if self.stop_button.isChecked() or self.stop_button_2.isChecked():
                self.stop_button.setChecked(False)
                self.stop_button.setCheckable(False)
                self.stop_button_2.setChecked(False)
                self.stop_button_2.setCheckable(False)
                self.both_dialogues("Stopsignal wird an die Datenaufnahme und -verarbeitung gesendet...\n")

                self.both_dialogues("GUI wird heruntergefahren...\n")
                client.close()
                self.both_dialogues("Verbindung zur Datenbank beendet...\n")
                sys.exit()

    def LED_states(self, led_state):
        self.LED_an_Zustand_1.hide()
        self.LED_an_Zustand_2.hide()
        self.LED_an_Zustand_3.hide()
        self.LED_an_Zustand_11.hide()
        self.LED_an_Zustand_21.hide()
        self.LED_an_Zustand_31.hide()
        if led_state == 1:
            self.LED_an_Zustand_1.show()
            self.LED_an_Zustand_11.show()
        if led_state == 2:
            self.LED_an_Zustand_2.show()
            self.LED_an_Zustand_21.show()
        if led_state == 3:
            self.LED_an_Zustand_3.show()
            self.LED_an_Zustand_31.show()

    def machine_learning_training(self):
        self.both_dialogues("Der Algorithmus für das maschinelle Lernen wird trainiert...\n")
        df_train_data = pd.read_csv("ML_Train_Data.csv")

        split_factor = 0.9
        X = df_train_data.iloc[:, 1:52].values
        y = df_train_data.iloc[:, 52].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_factor, random_state=1, stratify=y)

        sc = StandardScaler()
        sc.fit(X_train)
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)

        classifier = MLPClassifier(solver="adam", alpha=0.2, max_iter=5000, early_stopping=False)
        classifier.fit(X_train_std, y_train)
        predicted = classifier.predict(X_test_std)
        print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(y_test, predicted)))
        self.both_dialogues("Das Training des maschinellen Lernens ist abgeschlossen\n")
        return sc, classifier

    def machine_learning_classification(self, sc, classifier, df_new_data):
        freq_data_1, x_time, x_freq = gen_test_data(df_new_data[len(df_new_data)-102:])
        freq_data_2, x_time, x_freq = gen_test_data(df_new_data[len(df_new_data)-204:len(df_new_data)-102])
        freq_data_3, x_time, x_freq = gen_test_data(df_new_data[len(df_new_data) - 306:len(df_new_data) - 204])
        classification_set_1 = np.delete(freq_data_1, 0)
        classification_set_2 = np.delete(freq_data_2, 0)
        classification_set_3 = np.delete(freq_data_3, 0)
        classification_set = np.vstack((classification_set_1, classification_set_2, classification_set_3))
        classification_data = sc.transform(classification_set)
        predicted = classifier.predict(classification_data)
        probability = classifier.predict_proba(classification_data)
        if predicted[0] == predicted[1] and predicted[0] == predicted[2]:
            predicted_state = predicted[0]
        elif probability[0][predicted[0]-1] > probability[1][predicted[1]-1] and probability[0][predicted[0]-1] > probability[2][predicted[2]-1]:
            predicted_state = predicted[0]
            self.textBrowser.setTextColor(QColor(255, 0, 0))
            self.both_dialogues("Keine eindeutige Bestimmung des aktuellen Status möglich.\nDie Wahrscheinlichkeit der vorhergesagten Klasse beträgt: " + str(probability[0][predicted[0]-1]*100)+"%")
            self.textBrowser.setTextColor(QColor(255, 255, 255))
        elif probability[0][predicted[0]-1] < probability[1][predicted[1]-1] and probability[1][predicted[1]-1] > probability[2][predicted[2]-1]:
            predicted_state = predicted[0]
            self.textBrowser.setTextColor(QColor(255, 0, 0))
            self.both_dialogues("Keine eindeutige Bestimmung des aktuellen Status möglich.\nDie Wahrscheinlichkeit der vorhergesagten Klasse beträgt: " + str(probability[1][predicted[0]-1]*100)+"%")
            self.textBrowser.setTextColor(QColor(255, 255, 255))
        elif probability[0][predicted[0]-1] < probability[2][predicted[2]-1] and probability[1][predicted[1]-1] < probability[2][predicted[2]-1]:
            predicted_state = predicted[0]
            self.textBrowser.setTextColor(QColor(255, 0, 0))
            self.both_dialogues("Keine eindeutige Bestimmung des aktuellen Status möglich.\nDie Wahrscheinlichkeit der vorhergesagten Klasse beträgt: " + str(probability[2][predicted[0]-1]*100)+"%")
            self.textBrowser.setTextColor(QColor(255, 255, 255))
        elif probability[0][predicted[0]-1] == probability[1][predicted[1]-1] and probability[0][predicted[0]-1] == probability[2][predicted[2]-1]:
            predicted_state = predicted[0]
            self.textBrowser.setTextColor(QColor(255, 0, 0))
            self.both_dialogues(
                "Keine eindeutige Bestimmung des aktuellen Status möglich.\nDie Wahrscheinlichkeit der vorhergesagten Klasse beträgt: " + str(
                    probability[0][predicted[0] - 1] * 100) + "%")
            self.textBrowser.setTextColor(QColor(255, 255, 255))
        self.LED_states(led_state=predicted_state)

########################################################################################################################
# Connection to Mongo DB                                                                                               #
########################################################################################################################


client = MongoClient("mongodb+srv://dlsp:dlsp@cluster0.6jkhj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.DLSP
collection = db.Accel
app = QApplication(sys.argv)
win = Window()
thread_update = threading.Thread(target=win.update_chart)
thread_update.start()
external_chart()

while True:
    win.show()
    sys.exit(app.exec())
