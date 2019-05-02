#SQLInit

import sqlite3
import plotSql

##### creez connection 
conn = sqlite3.connect("GreenFarm.db", check_same_thread=False)
c = conn.cursor()



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
        
def moist_sql(moist):
    print("Inserted Moisture in DB")
    hum = 0
    temp = 0

    insert_value(hum, temp, moist)

def insert_value(hum, temp, moist):

    print("Moist = ", moist)
    c.execute(" INSERT INTO GF_Value(humidity , temperature, moisture) VALUES (? , ?, ?) "   , (hum,temp,moist)) 
    print("Inserted")
    conn.commit()
    
    #print("Read value = ")
    