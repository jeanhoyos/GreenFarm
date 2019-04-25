#include <SimpleDHT.h>

int pinDHT11 = 2;   // humidity and temperature of ambient air
SimpleDHT11 dht11; 
int temp=0;

void setup() {
  // put your setup code here, to run once:
   pinMode(2, OUTPUT);
   Serial.begin(9600);   //Sets the baud for serial data transmission 

}

void loop() {
  // put your main code here, to run repeatedly:
  
  // Serial.print("Temperature:"); 
   byte temperature = 20;
   byte humidity = 80;
   byte data[40] = {0};
   
   //if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
   //Serial.println("Read DHT11 failed");
    //return;
    //}
    
   //temp=(int)temperature;
  // Serial.print(temperature);
  // Serial.print(',');
  // Serial.print(humidity) ;
  
  
   delay(1000);
   digitalWrite(2, HIGH); // sets the digital pin 13 on
  delay(1000);            // waits for a second
  digitalWrite(2, LOW);  // sets the digital pin 13 off
  delay(1000);            // waits for a second
  byte data_rasp = Serial.read();
  Serial.print(data_rasp);
  

}
