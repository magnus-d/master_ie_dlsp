##################################################################################
# Import of the required libraries and files #####################################
##################################################################################
import socket
import pandas
import gui_dlsp
from PySide6.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox)
import PySide6
from PySide6 import QtCharts
import sys
import matplotlib.pyplot as plt
import threading
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads

##################################################################################
# Declaration of variables #######################################################
##################################################################################
data_string = ""
accel_data = []
timestamp = []

##################################################################################
# Initializing TCP server & Mongo DB for data transmission #######################
##################################################################################
client = MongoClient("localhost:27017")
db = client.DLSP

TCP_IP = #####
TCP_PORT = #####
BUFFER_SIZE = 15000
print("Trying to establish connection")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print("Waiting for ESP")
s.listen(1)
conn, addr = s.accept()
print('Connection address:', addr)

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    data_string += data.decode()
    data_string_cache = data_string.replace(' ', '').replace('),', ')').replace('(', '').replace('[', '')
    data_string_cache = list(data_string_cache.split(')'))
    data_string = ''

    index = 0
    while index + 1 < len(data_string_cache):
        data_record = data_string_cache[index] + "," + data_string_cache[index+1]
        data_record = list(data_record.split(","))
        print(data_record)
        if len(data_record) == 10:
            timestamp.append(data_record[3:])
            accel_data.append(data_record[:3])
        index = index + 2
    print(accel_data)
    print(timestamp)
    if len(accel_data) > 0:
        db.Test.insert_many([{'time': timestamp[i], 'Accel': accel_data[i]} for i in range(len(accel_data))])
    accel_data.clear()
    timestamp.clear()
conn.close()
print("TCP Server terminated")
db.close()
print("Connection to MongoDB terminated")
