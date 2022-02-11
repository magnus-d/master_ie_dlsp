########################################################################################################################
# Import of the required libraries and files                                                                           #
########################################################################################################################
from machine import Pin, I2C, Timer, RTC
from imu import MPU6050
import time
from machine import Pin
import network
import files
import ntptime
import socket

########################################################################################################################
# Show the files flashed on the micropython device                                                                     #
########################################################################################################################
files

########################################################################################################################
# Define useful functions for the following program                                                                    #
########################################################################################################################
def current_time():
    # This function is used to measure the current time after it was synchronized
    dt = RTC().datetime()
    dt = dt[:3] + dt[4:]
    return dt

def wifi_connect():
    # This function is used to establish wifi connection and synchronize the time using the network
    print("Connecting to WIFI")
    WIFI_SSID = "Area51_DG_24"
    WIFI_PW = "DaismeprWLKe$%&2108"

    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(WIFI_SSID, WIFI_PW)
        while not wlan.isconnected():
            pass
    print("connected:", WIFI_SSID)
    time.sleep(1)
    ntptime.settime()

def read_imu(tim):
    try:
        global DataCounter
        global accel
        if DataCounter == 0:
            dt = current_time()
            timestamp = str(dt[0]) + "," + str(dt[1]) + "," + str(dt[2]) + "," + str(dt[3]) + "," + str(dt[4]) + "," + str(
                dt[5]) + "," + str(dt[6]) + ")"
            TCP_socket.send(timestamp.encode())
        TCP_socket.send(str(accel.xyz).encode())
        DataCounter = DataCounter + 1
        if DataCounter == 200:
            DataCounter = 0
    except OSError:
        tim.deinit()
        print("TCP connection terminated. Preparing Microcontroller to shut down")
        TCP_socket.close()

########################################################################################################################
# Connect to wifi / Initialize the required variables and lists                                                        #
########################################################################################################################
wifi_connect()
DataCounter = 0
TCP_IP = '10.128.15.39'
#TCP_IP = '10.128.15.36'
TCP_PORT = 8000
BUFFER_SIZE = 15000
connection_status = False

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
mpu6050 = MPU6050(i2c)
accel = mpu6050.accel
tim = Timer(-1)

while not connection_status:
    print("Trying to connect via TCP")
    try:
        TCP_socket = socket.socket()
        addrinfos = socket.getaddrinfo(TCP_IP, TCP_PORT)
        TCP_socket.connect(addrinfos[0][4])
        connection_status = True
        print("TCP connection established. Starting measurement")
    except OSError:
        print("Failed to connect. Please wait...")
        time.sleep(5)
tim.init(period=10, mode=Timer.PERIODIC, callback=read_imu)