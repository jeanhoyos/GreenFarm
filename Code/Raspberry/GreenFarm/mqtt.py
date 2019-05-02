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
    print("message received",m_decode)
    print(topic)
    if topic == "GreenFarm/Arduino/Moist":
        SQLInit.moist_sql(m_decode)
    

    
    

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
    time.sleep(2)
    print("Initialized", broker)

def connect():
    client.connect(broker)
    print("Connected")
    
def start():
    
    client.loop_forever()
    print("Started to listen")



#connect()
#init()
#start()

#client.loop_start()
#time.sleep(4)
#lient.loop_stop()
#print("stopped")

"""
SQL
"""


#read_data()
#c.close()
#conn.close()



#time.sleep(4)


#client.disconnect()