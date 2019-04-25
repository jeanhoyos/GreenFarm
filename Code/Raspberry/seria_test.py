import serial

import time
ser = serial.Serial('/dev/ttyACM0',9600)




while True:
   # temp = str(ser.read(5).decode('ascii'))
   # temp.split(',')
   # print(temp)
   # temp,humidity = [int(s) for s in temp.split(',')]
   # print('temperature = {}'.format(temp))
   # print('humidity = {}'.format(humidity))
    
    counter="1"
    ser.write(bytes([2]))
    print("sending")
    
    time.sleep(3)
    #TEST YIOLIL





