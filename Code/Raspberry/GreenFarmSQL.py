import sqlite3
import random


##### creez connection 
conn = sqlite3.connect("GreenFarm.db")
c = conn.cursor()


### Fonction 
def Create_table():
    c.execute("CREATE TABLE IF NOT EXISTS GF_Value(humidity REAL ,temperature  REAL, moisture REAL) ")

def del_value():
    c.execute("DELETE FROM Values")
    conn.commit()

   
def read_data():
    #c.execute(""" SELECT * FROM Valeurs WHERE °C > 0 """)
    c.execute(""" SELECT * FROM GF_Value """)
    data = c.fetchall()
    for row in data:
        print(row)


def insert_value(hum, temp, moist):

    print("Here")
    c.execute(" INSERT INTO GF_Value(humidity , temperature, moisture) VALUES (? , ?, ?) "   , (hum,temp,moist)) 
    print("Inserted")
    conn.commit()


#### MAIN
Create_table()
#del_value()

hum = 3
temp = 5
moist = 19

insert_value(hum, temp, moist)
read_data()
c.close()

conn.close()
