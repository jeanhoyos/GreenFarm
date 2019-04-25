import sqlite3
import random


##### creez connection 
conn = sqlite3.connect("test.db")
c = conn.cursor()


### Fonction 
def Create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Valeurs(humidité REAL , °C REAL) ")

def del_value():
    c.execute("DELETE FROM Valeurs")
    conn.commit()
  

def random_value():
    val1 = random.randrange(1,10)
    val2 = random.randrange(1,8)
    c.execute(" INSERT INTO Valeurs(humidité , °C ) VALUES (? , ?) "   , (val1,val2))
    conn.commit()
   
def read_data():
    c.execute(""" SELECT * FROM Valeurs WHERE °C > 0 """)
    data = c.fetchall()
    for row in data:
        print(row)
    print("ye")    


#### MAIN
Create_table()
del_value()

for i in range(5):
    random_value()
read_data()
c.close()
print("hello")
conn.close()