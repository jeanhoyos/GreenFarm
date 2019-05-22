import plotSql
import SQLInit
import MoistControl
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
#plotSql.plot_data()  # carefull you have to close the window to receive data

#MQTT

mqtt.connect()
mqtt.init()




"""
Main used to check that connection is maintained. Relaunch if necessary 
"""

while(True):
    print("Listening")
    
    MoistControl.control_moisture()
    
    time.sleep(10)
    
    
    

    
    
    