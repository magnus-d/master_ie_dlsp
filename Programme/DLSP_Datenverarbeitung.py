########################################################################################################################
# Import of the required libraries and files                                                                           #
########################################################################################################################
import socket
from pymongo import MongoClient

########################################################################################################################
# Declaration of variables                                                                                             #
########################################################################################################################
data_string = ""
accelx_data = []
accely_data = []
accelz_data = []
timestamp = []
data_list = []

########################################################################################################################
# Initializing TCP server & Mongo DB for data transmission                                                             #
########################################################################################################################
client = MongoClient("mongodb+srv://dlsp:dlsp@cluster0.6jkhj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.DLSP

TCP_IP = '***'
TCP_PORT = 8000
BUFFER_SIZE = 15000
print("Trying to establish connection")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print("Waiting for ESP")
s.listen(1)
conn, addr = s.accept()
print('ESP connected\nConnection address:', addr)

while True:
    data = conn.recv(BUFFER_SIZE)
    string_received_data = data.decode()
    data_list.append(string_received_data)
    if not data:
        break
    if len(data_list) > 199:
        for record in data_list:
            data_string = record.replace(' ', '').replace('(', '')
            data_string = list(data_string.split(')'))

            for index in range(len(data_string)):
                data_record = list(data_string[index].split(","))

                if len(data_record) == 7:
                    time_record = data_record

                elif len(data_record) == 3:
                    if 2 < len(data_record[0]) < 9 and 2 < len(data_record[1]) < 9 and 2 < len(data_record[2]) < 9:
                        accelx_data.append(data_record[0])
                        accely_data.append(data_record[1])
                        accelz_data.append(data_record[2])
                        timestamp.append(time_record[:])
                        time_record[6] = str(int(time_record[6]) + 10)
                        if int(time_record[6]) > 999:
                            time_record[5] = str(int(time_record[5]) + 1)
                            time_record[6] = str(int(time_record[6]) - 1000)
                            if int(time_record[5]) > 59:
                                time_record[4] = str(int(time_record[5]) + 1)
                                time_record[5] = str(int(time_record[6]) - 60)
                                if int(time_record[4]) > 59:
                                    time_record[3] = str(int(time_record[5]) + 1)
                                    time_record[4] = str(int(time_record[6]) - 60)
                                    if int(time_record[3]) > 23:
                                        time_record[2] = str(int(time_record[5]) + 1)
                                        time_record[3] = str(int(time_record[6]) - 24)
        data_list.clear()
        db.Accel.insert_many([{'time': timestamp[i], 'Ax': accelx_data[i], 'Ay': accely_data[i], 'Az': accelz_data[i]} for i in range(len(accelx_data))])
        accelx_data.clear()
        accely_data.clear()
        accelz_data.clear()
        timestamp.clear()
conn.close()
print("TCP Server terminated")
client.close()
print("Connection to MongoDB terminated")
