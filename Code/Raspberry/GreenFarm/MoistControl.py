#MoistControl


import SQLInit
import mqtt


def control_moisture():
    
    moist_avg = SQLInit.get_avg_moist_10()
    print("moist avg = ")
    print(moist_avg)
    
    if (moist_avg < 20):
        mqtt.send_pump_command("1")
        print("Sending command")
    else :
        mqtt.send_pump_command("0")
        print("No need to pump")
    