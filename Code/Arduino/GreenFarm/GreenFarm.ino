//#include <ArduinoNATS.h>

#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>

//DTH22
#include <Adafruit_Sensor.h>
#include <DHT.h>

// Function prototypes
void subscribeReceive(char* topic, byte* payload, unsigned int length);
 
// Set your MAC address and IP address here
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
// IP du shield run DHCPAdressPrinter
IPAddress ip(192, 168, 1, 21);
//IPAddress ip(Ethernet.localIP());
 
// Make sure to leave out the http and slashes!
//const char* server = "test.mosquitto.org";
const char *serverHostname = "raspberrypi";
const IPAddress serverIPAddress(192, 168, 1, 2);

EthernetClient ethClient;
PubSubClient mqttClient(ethClient);


// Mqtt topics definition
const char *pub_temp = "GreenFarm/Arduino/Temperature";
const char *pub_hum = "GreenFarm/Arduino/Humidity";
const char *pub_moist = "GreenFarm/Arduino/Moist";


const char *sub_window = "GreenFarm/Raspberry/Window  ";
const char *sub_pump = "GreenFarm/Raspberry/Pumping";

//Arduino 

// constants won't change. Used here to set a pin number:
const int ledPin = 2;// the number of the LED pin
// Variables will change:
int ledState = LOW;             // ledState used to set the LED

//Constants DTH22
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino




void setup(){

    // Useful for debugging purposes
  Serial.begin(9600);

  dht.begin();
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);

/**
 *  Ethernet and Mqtt server
 *  
 *  Server run on raspberry pi : hostname raspberrypi and ip = 193.168.1.4
 *  
 *  
 */
  
  // Start the ethernet connection
  Ethernet.begin(mac, ip);
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }        
  Serial.println("Connected to shield") ;  
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }
  Serial.println("Cable connected") ;  
  // Ethernet takes some time to boot!
  delay(3000);                          

  // Set the MQTT server to the server stated above ^
  mqttClient.setServer(serverIPAddress, 1883);
  Serial.println("Connecting ...");
  while (!mqttClient.connect("myClientID")) {
    delay(1000);
  }
  Serial.println("Connected ! ");
    // Establish the subscribe event
  mqttClient.setCallback(subscribeReceive);

/**
 *  Green Farm configuration
 *  
 */
  
  

  
}

void loop(){
 // This is needed at the top of the loop!
  mqttClient.loop();
 
  // Subscribe to Raspberry Pump topic
  mqttClient.subscribe(sub_pump);
  mqttClient.subscribe(sub_window);


  // Soil Moisture

  int sensorValue = analogRead(A0);
  int sensorValue_map = map(sensorValue, 1023, 0, 0, 100);
  // print out the value you read:
  Serial.print("Humidity: ");
  Serial.print(sensorValue_map);
  Serial.println("%");

    //Read data and store it to variables hum and temp
    float hum;  //Stores humidity value
    float temp; //Stores temperature value
    hum = dht.readHumidity();
    temp= dht.readTemperature();
    //Print temp and humidity values to serial monitor
    Serial.print("Humidity: ");
    Serial.print(hum);
    Serial.print(" %, Temp: ");
    Serial.print(temp);
    Serial.println(" Celsius"); 
 
  // Publish Moisture on Server"
  
  String moist_str = (String)sensorValue_map;
  char moist_char[moist_str.length() + 1];
  moist_str.toCharArray(moist_char, moist_str.length() + 1);

  String hum_str = (String)hum;
  char hum_char[hum_str.length()+1];
  hum_str.toCharArray(hum_char, hum_str.length() + 1);

 
  String temp_str = (String)temp;
  char temp_char[temp_str.length()+1];
  temp_str.toCharArray(temp_char, temp_str.length() + 1);

  
  if(mqttClient.publish(pub_moist, moist_char))
  {
    Serial.println("published message");
    Serial.println(pub_moist);
  }
  else
  {
    Serial.println("Could not send moist message :(");
  }
  // Publish Temperature on Server"
    if(mqttClient.publish(pub_temp, temp_char))
  {
    Serial.println("published message");
    Serial.println(pub_temp);
  }
  else
  {
    Serial.println("Could not send temp message :(");
  }
  // Publish Humidity on Server"
 
   
    if(mqttClient.publish(pub_hum, hum_char))
  {
    Serial.println("published message");
    Serial.println(pub_hum);
  }
  else
  {
    Serial.println("Could not send hum message :(");
  }
  

  
 
  // Dont overload the server!
  delay(10000);
    


  
}



void pump_control(String data){
    int pump_value = data.toInt();
    Serial.println(pump_value);

    if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
    }

    Serial.print("Led state = ");
    Serial.println(ledState);

    // set the LED with the ledState of the variable:
    digitalWrite(ledPin, ledState);
  
  }

void subscribeReceive(char* topic, byte* payload, unsigned int length)
{
  // Print the topic
  Serial.print("Topic: ");
  Serial.println(topic);
 
  // Print the message
  Serial.print("Received Message: ");
  //char *data = "";
  String value = "";
  for(int i = 0; i < length; i ++)
  {
    //Serial.print(char(payload[i]));
    value += char(payload[i]);
  }
  Serial.println("");
  Serial.print("Data = ");
  Serial.println(value);

 
  if (strcmp (topic,"GreenFarm/Raspberry/Pumping") == 0){
    pump_control(value);
    Serial.println("Received Pump order");
    }
  else if (strcmp (topic,"GreenFarm/Raspberry/Window") == 0){
    Serial.println("Received  Window order");
    }
  else{
      Serial.println("nothing");
    }

/*
  switch (char(topic)){
    
    case  char(sub_pump:

      break;

    case sub_window:

      break;
    }

*/

  

  
  
 
  // Print a newline
  Serial.println("");
}
