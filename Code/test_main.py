##################################################################################
# Import of the required libraries and files #####################################
##################################################################################
from machine import Pin, I2C, Timer, RTC
from imu import MPU6050
import time
from machine import Pin
import network
import files
import ntptime
import socket

##################################################################################
# Show the files flashed on the micropython device ###############################
##################################################################################
files

##################################################################################
# Define useful functions for the following program ##############################
##################################################################################
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

    # print("connected:", WIFI_SSID, wlan.ifconfig())
    print("connected:", WIFI_SSID)
    time.sleep(1)
    ntptime.settime()

def read_imu(tim):
    # This function is used to measure the acceleration data and get the current time as callback function of the timer
    global DataCounter
    accel = mpu6050.accel
    dt = current_time()
    sensor_data.append(accel.xyz)
    sensor_data.append(dt)
    DataCounter = DataCounter+1

##################################################################################
# Connect to wifi / Initialize the required variables and lists ##################
##################################################################################
wifi_connect()
sampling_rate = 10
sensor_data = []
sensor_data_2 = []
DataCounter = 0
TCP_IP = '10.128.15.39'
TCP_PORT = 8000
BUFFER_SIZE = 15000

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
mpu6050 = MPU6050(i2c)
tim = Timer(-1)
print("Trying to connect via TCP")
TCP_socket = socket.socket()
addrinfos = socket.getaddrinfo(TCP_IP, TCP_PORT)
TCP_socket.connect(addrinfos[0][4])
print("TCP connection established. Starting measurement")
tim.init(period=sampling_rate, mode=Timer.PERIODIC, callback=read_imu)

##################################################################################
# While-loop for continuous measuring as long as the GUI is active ###############
##################################################################################
while True:
    if DataCounter > 75:
        TCP_socket.send(str(sensor_data).encode())
        sensor_data.clear()
        DataCounter = 0
tim.deinit()
