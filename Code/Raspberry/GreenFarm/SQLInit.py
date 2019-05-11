#SQLInit

import sqlite3
import plotSql
import datetime
import time

##### creez connection 
conn = sqlite3.connect("GreenFarm.db", check_same_thread=False)
c = conn.cursor()

print("+++++++++++++++++++++++++++++++++++")
temp_global = 0
hum_global = 0
moist_global = 0

### Fonction SQL
def Create_table():
    c.execute("CREATE TABLE IF NOT EXISTS GF_Value(id INT AUTO_INCREMENT PRIMARY KEY, humidity REAL ,temperature  REAL, moisture REAL, cur_timestamp TIMESTAMP(8))")

def del_value():
    c.execute("DELETE FROM GF_Values")
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
        
def moist_sql(moist):
    global moist_global
    moist_global = moist
    
    insert_value(hum_global, temp_global, moist_global)

def hum_sql(hum):
    global hum_global
    hum_global = hum
    insert_value(hum_global, temp_global, moist_global)
    
def temp_sql(temp):
    global temp_global
    temp_global = temp
    insert_value(hum_global, temp_global, moist_global)

def insert_value(hum, temp, moist):

    if(hum_global == 0 or temp_global == 0 or moist_global == 0):
        print("hum = ", hum_global)
        print("temp = ", temp_global)
        print("moist = " , moist_global)
        print("Waiting for all data")
    else:
        print("hum = ", hum_global)
        print("temp = ", temp_global)
        print("moist = " , moist_global)
        #time = c.execute("SELECT CURRENT_TIMESTAMP")
        #date = datetime.datetime.now()#.timestamp()
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print(timestamp)
        print("Inserting")
        c.execute(" INSERT INTO GF_Value(humidity , temperature, moisture, cur_timestamp) VALUES (? , ?, ?, ?) "   , (hum_global,temp_global,moist_global, timestamp)) 
        conn.commit()
        print("Inserted")
        global hum_global
        global temp_global
        global moist_global
        hum_global = 0
        temp_global = 0
        moist_global = 0
        print("SET to O")
    
    
    #print("Read value = ")
def get_avg_moist_10():
    ("")
    