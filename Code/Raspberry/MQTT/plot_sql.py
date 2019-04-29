import sqlite3
from matplotlib import pyplot as plt   
   
##### creez connection 
conn = sqlite3.connect("GreenFarm.db", check_same_thread=False)
c = conn.cursor()

## Data list for plot
temp = [];
time = [];   
   
   
plot_GLOBAL = True
   
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
                    
    print("time list = ")
    print(time)                
            
    print("temp list = ")
    print(temp)
    print("------------------------------------------------------------------")
    plot_value = plot_GLOBAL
    print(plot_value)
    
    if (plot_value):
        plot_value = False
        print("plot *******************************************")
        plt.plot(time,temp)
        plt.show()
        
        
read_data()
        