########################################################################################################################
# READ-ME!                                                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
# Bevor die Klassifizierung durchgeführt werden kann, müssen die Zeitpunkte dem jeweiligen Waschprogramm angepasst     #
# werden, damit die vergebenen Klassifizierung auch sinnvoll sind. Außerdem sollte vorher geprüft werden, ob die       #
# aufgenommenen Werte auch wirklich dem Zweck entsprechen.                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
# Zustände:                                                                                                            #
#   1 | Stillstand                                                                                                     #
#   2 | Spülen                                                                                                         #
#   3 | Vorwäsche                                                                                                      #
#   4 | Waschen                                                                                                        #
#   5 | Schleudern                                                                                                     #
########################################################################################################################

from pymongo import MongoClient
import pandas as pd

client = MongoClient("localhost:27017")
db = client.DLSP
collection = db.Machine_Learning
new_collection = db.ML_Train_Data
classification_list = []
ax = []
ay = []
az = []
counter_stillstand = 0
counter_spülen = 0
counter_vorwäsche = 0
counter_waschen = 0
counter_schleudern = 0
counter_defekte = 0

df_data = pd.DataFrame(list(collection.find()))
print("Zu klassifizierendes Dataframe: \n", df_data)
start_time = df_data["time"][0]

for i in range(len(df_data)):
    time_scaled = (int(df_data["time"][i][3]) - int(start_time[3])) * 60 * 60 + (
                          int(df_data["time"][i][4]) - int(start_time[4])) * 60 + (
                          int(df_data["time"][i][5]) - int(start_time[5])) + (
                          int(df_data["time"][i][6]) - 0) / 1000
    time_scaled = round(time_scaled, 3)
    if time_scaled < 0:
        counter_defekte = counter_defekte + 1

    elif time_scaled < 275 or 315 <= time_scaled < 343 or 1215 <= time_scaled < 1271 or 1298 <= time_scaled < 1440 \
            or 8995 <= time_scaled < 9390 or 9709 <= time_scaled:
        classification_list.append(2)  # Spülen
        ax.append(df_data["Ax"][i])
        ay.append(df_data["Ay"][i])
        az.append(df_data["Az"][i])
        counter_spülen = counter_spülen + 1
    elif 352 <= time_scaled < 400 or 408 <= time_scaled < 416 or 426 <= time_scaled < 1140:
        classification_list.append(3)  # Vorwäsche
        ax.append(df_data["Ax"][i])
        ay.append(df_data["Ay"][i])
        az.append(df_data["Az"][i])
        counter_vorwäsche = counter_vorwäsche + 1
    elif 1140 <= time_scaled < 1215 or 8740 <= time_scaled < 8995 or 9480 <= time_scaled < 9709:
        classification_list.append(5)  # Schleudern
        ax.append(df_data["Ax"][i])
        ay.append(df_data["Ay"][i])
        az.append(df_data["Az"][i])
        counter_schleudern = counter_schleudern + 1
    elif time_scaled < 2096 or 2134 <= time_scaled < 2162 or 8105 <= time_scaled < 8180:
        classification_list.append(1)  # Stillstand
        ax.append(df_data["Ax"][i])
        ay.append(df_data["Ay"][i])
        az.append(df_data["Az"][i])
        counter_stillstand = counter_stillstand + 1
    else:
        classification_list.append(4)  # Waschen
        ax.append(df_data["Ax"][i])
        ay.append(df_data["Ay"][i])
        az.append(df_data["Az"][i])
        counter_waschen = counter_waschen + 1
db.ML_Train_Data.insert_many([{"Ax": ax[i], "Ay": ay[i], "Az": az[i], "Classification": classification_list[i]} for i in range(len(classification_list))])
print("Übersicht der Klassifizierungsergebnisse:")
print("Stillstand: ", counter_stillstand)
print("Spülen: ", counter_spülen)
print("Vorwäsche: ", counter_vorwäsche)
print("Waschen: ", counter_waschen)
print("Schleudern: ", counter_schleudern)
print("\n Defekte Datensätze: ", counter_defekte)
