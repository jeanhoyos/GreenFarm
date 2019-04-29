#//https://www.youtube.com/watch?v=QAaXNt0oqSI

import time
import paho.mqtt.client as mqtt
import sqlite3
from matplotlib import pyplot as plt

##### creez connection 
conn = sqlite3.connect("GreenFarm.db", check_same_thread=False)
c = conn.cursor()

## Data list for plot
temp = [];
time = [];


### Fonction SQL
def Create_table():
    c.execute("CREATE TABLE IF NOT EXISTS GF_Value(humidity REAL ,temperature  REAL, moisture REAL) ")

def del_value():
    c.execute("DELETE FROM Values")
    conn.commit()

   
def read_data():
    #c.execute(""" SELECT * FROM Valeurs WHERE °C > 0 """)
    c.execute(""" SELECT * FROM GF_Value """)
    data = c.fetchall()
    
    temp = []
    time = []
    
    i = 1;
    for row in data:
        time.append(i)
        i = i +1
        count = 0
        for el in row:
            if(count == 2):
                temp.append(int(el))
            count = count + 1
                    
    print("time list = ")
    print(len(time))                
            
    print("temp list = ")
    print(len(temp))
    print("------------------------------------------------------------------")
    plot_value = plot_GLOBAL
    print(plot_value)
    
    if (plot_value):
        plot_value = False
        print("plot *******************************************")
        #plt.plot(time, temp)
        #plt.show()
        

def insert_value(hum, temp, moist):

    print("Moist = ")
    print(moist)
    c.execute(" INSERT INTO GF_Value(humidity , temperature, moisture) VALUES (? , ?, ?) "   , (hum,temp,moist)) 
    print("Inserted")
    conn.commit()
    
    #print("Read value = ")
    read_data()

## MQTT Functions

def On_Log(client,userdata,level,buf):
    print("log: "+buf)
    
def On_Connect(client, userdata, flags,rc):
    if rc==0:
        print("connection ok ")
    else :
        print("bad connection for", rc)

def On_Disconnect(client, userdata, flags, rc=0):
    print("Disco too :"+str(rc))
def On_message(client,userdata,msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8"))
    print("message received",m_decode)
    print(topic)
    if topic == "GreenFarm/Arduino/Moist":
        moist_sql(m_decode)
    
def moist_sql(moist):
    print("Inserted Moisture in DB")
    hum = 0
    temp = 0

    insert_value(hum, temp, moist)
    
    

"""
MQTT server connection
"""
Create_table()

plot_GLOBAL = True
print("************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(plot_GLOBAL)
broker ="192.168.1.5"
client=mqtt.Client("python-mqtt")
client.on_connect=On_Connect
client.on_log=On_Log
client.on_message=On_message

client.on_disconnect=On_Disconnect
print("connected", broker)
client.connect(broker)
client.loop_start()
client.subscribe("GreenFarm/Arduino/Moist")
#time.sleep(1)
#client.publish("GreenFarm/Arduino/Humidity","hello")
client
print("In the loop")



"""
SQL
"""


#read_data()
#c.close()
#conn.close()



#time.sleep(4)


#client.disconnect()