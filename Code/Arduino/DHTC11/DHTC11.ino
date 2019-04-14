#include <SimpleDHT.h>

int pinDHT11 = 2;   // humidity and temperature of ambient air
SimpleDHT11 dht11; 
int temp=0;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);   //Sets the baud for serial data transmission 

}

void loop() {
  // put your main code here, to run repeatedly:
  
  // Serial.print("Temperature:"); 
   byte temperature = 0;
   byte humidity = 0;
   byte data[40] = {0};
   
   if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
    Serial.println("Read DHT11 failed");
    return;
    }
   temp=(int)temperature;
   Serial.print(temp);
   Serial.print(',');
   Serial.print(humidity) ;
   delay(1200);
  

}
