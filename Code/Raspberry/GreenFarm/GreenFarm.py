import plotSql
import SQLInit
#from mqtt import *
import time
import mqtt



"""
Init
Connect

"""

print("Start")

#SQL
SQLInit.Create_table()
# Plot previous data
#plotSql.plot_data()
#MQTT

mqtt.connect()
mqtt.init()
mqtt.start()



"""
Main used to check that connection is maintained. Relaunch if necessary 
"""

while(True):
    print("Listening")
    time.sleep(4)
    
    
    

    
    
    