//#include <ArduinoNATS.h>

#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>


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
const IPAddress serverIPAddress(192, 168, 1, 5);

EthernetClient ethClient;
PubSubClient mqttClient(ethClient);


// Mqtt topics definition
const char *pub_temp = "GreenFarm/Arduino/Temperature";
const char *pub_hum = "GreenFarm/Arduino/Humidity";
const char *pub_moist = "GreenFarm/Arduino/Moist";

char *sub_window = "GreenFarm/Raspberry/Window  ";
char *sub_pump = "GreenFarm/Raspberry/Pump";

//Arduino 

// constants won't change. Used here to set a pin number:
const int ledPin = 2;// the number of the LED pin
// Variables will change:
int ledState = LOW;             // ledState used to set the LED



void setup(){

    // Useful for debugging purposes
  Serial.begin(9600);


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
  Serial.print(sensorValue_map);
  Serial.println("%");
 
  // Publish Temperature on Server"
  
  String temp_str = (String)sensorValue_map;
  char char_array[temp_str.length() + 1];
  temp_str.toCharArray(char_array, temp_str.length() + 1);
  if(mqttClient.publish(pub_moist, char_array))
  {
    Serial.println("published message");
  }
  else
  {
    Serial.println("Could not send message :(");
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

 
  if (strcmp (topic,"GreenFarm/Raspberry/Pump") == 0){
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
