//https://www.youtube.com/watch?v=QAaXNt0oqSI

import time
import paho.mqtt.client as mqtt

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



broker ="192.168.1.4"
client=mqtt.Client("python-mqtt")
client.on_connect=On_Connect
client.on_log=On_Log
client.on_message=On_message

client.on_disconnect=On_Disconnect
print("connected", broker)
client.connect(broker)
client.loop_start()
client.subscribe("GreenFarm/Arduino/Temperature")
time.sleep(1)
client.publish("GreenFarm/Arduino/Humidity","hello")
client

time.sleep(4)
client.loop_stop()
client.disconnect()