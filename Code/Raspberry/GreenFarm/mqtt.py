#//https://www.youtube.com/watch?v=QAaXNt0oqSI

import time
import paho.mqtt.client as mqtt
import SQLInit



broker = "localhost"
#broker="broker.hivemq.com"
client=mqtt.Client("python-mqtt")


## MQTT Functions

def On_Log(client,userdata,level,buf):
    print("log: "+buf)
    
def On_Connect(client, userdata, flags,rc):
    if rc==0:
        print("connection ok ")
    else :
        print("bad connection for", rc)

def On_Disconnect(client, userdata, flags, rc=0):
    connect()
    print("Reconnection :"+str(rc))
    
def On_message(client,userdata,msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8"))
    if topic == "GreenFarm/Arduino/Moist":
        print("Moist = ", m_decode)
        if (m_decode == "1"):
            print("Glitch value stopped")
        else:
            SQLInit.moist_sql(m_decode)
    elif topic == "GreenFarm/Arduino/Temperature":
        print("Temperature = ", m_decode)
        SQLInit.temp_sql(m_decode)
        
    elif topic == "GreenFarm/Arduino/Humidity":
        print("Humidity = ", m_decode)
        SQLInit.hum_sql(m_decode)
    

def send_pump_command(pump_data):
    client.publish("GreenFarm/Raspberry/Pumping",pump_data)
    print("publish ppudmp data")
    print(pump_data)

"""
MQTT server connection
"""

def init():

    client.on_connect=On_Connect
    client.on_log=On_Log
    client.on_message=On_message
    client.on_disconnect=On_Disconnect
    client.loop_start()
    
    client.subscribe("GreenFarm/Arduino/Moist")
    client.subscribe("GreenFarm/Arduino/Temperature")
    client.subscribe("GreenFarm/Arduino/Humidity")
    time.sleep(2)
    print("Initialized", broker)

def connect():
    client.connect(broker)
    print("Connected")
    


