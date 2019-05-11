import sqlite3
from matplotlib import pyplot as plt
import datetime
import time
   
##### creez connection 
conn = sqlite3.connect("GreenFarm.db", check_same_thread=False)
c = conn.cursor()

## Data list for plot
temp = [];
hum = [];
moist = [];
time = [];   
   
   
plot_GLOBAL = True


def plot_data():
    #c.execute(""" SELECT * FROM Valeurs WHERE °C > 0 """)
    c.execute(""" SELECT temperature, humidity, moisture, cur_timestamp FROM GF_Value """)
    data = c.fetchall()
    print(data)
    temp = []
    time = []

    for row in data:
        temp.append(row[0])
        hum.append(row[1])
        moist.append(row[2])
        timestamp = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        time.append(timestamp)

    plot_value = plot_GLOBAL
    print(plot_value)
    
    if (plot_value):
        plot_value = False
        print("plot *******************************************")
        #plt.plot(time, temp, 'r', label='temp', time, hum, 'b', label='hum',time, moist, 'g',label='moist')
        plt.plot(time, temp, 'r', time, hum, 'b', time, moist, 'g')
        plt.ylabel('Temp - Hum - Moist')
        plt.xlabel('Time')
        #plt.plot(time,temp)
        plt.show()
        
plot_data()        
