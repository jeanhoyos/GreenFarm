//#include <ArduinoNATS.h>

#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>

// Function prototypes
void subscribeReceive(char* topic, byte* payload, unsigned int length);
 
// Set your MAC address and IP address here
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
// IP du shield run DHCPAdressPrinter

IPAddress ip(192, 168, 1, 14);

//IPAddress ip(Ethernet.localIP());
 
// Make sure to leave out the http and slashes!
const char* server = "test.mosquitto.org";
 //test.mosquitto.org/
// Ethernet and MQTT related objects
EthernetClient ethClient;
PubSubClient mqttClient(ethClient);
// jean ------>>  https://blog.rapid7.com/2016/10/07/logging-mosquitto-server-logs-from-raspberry-pi-to-logentries/



void setup(){

    // Useful for debugging purposes
  Serial.begin(9600);
  
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
  
  mqttClient.setServer(server, 1883);   


  Serial.println("Connecting ...");
  while (!mqttClient.connect("myClientID")) {
    delay(5000);
    Serial.println(Ethernet.localIP());
    Serial.println("be patient...");
  }
  Serial.println("Connected ! ");
  
 
  // Attempt to connect to the server with the ID "myClientID"
  if (mqttClient.connect("myClientID")) 
  {
    Serial.println("Connection has been established, well done");
 
    // Establish the subscribe event
    mqttClient.setCallback(subscribeReceive);
  } 
  else 
  {
    Serial.println("Looks like the server connection failed...");
  }
  
}

void loop(){
 // This is needed at the top of the loop!
  mqttClient.loop();
 
  // Ensure that we are subscribed to the topic "MakerIOTopic"
  mqttClient.subscribe("MakerIOTopic/message");
 
  // Attempt to publish a value to the topic "MakerIOTopic"
  if(mqttClient.publish("MakerIOTopic/message", "Arduino publish"))
  {
    Serial.println("Publish message success");
  }
  else
  {
    Serial.println("Could not send message :(");
  }

  
 
  // Dont overload the server!
  delay(4000);
    


  
}

void subscribeReceive(char* topic, byte* payload, unsigned int length)
{
  // Print the topic
  Serial.print("Topic: ");
  Serial.println(topic);
 
  // Print the message
  Serial.print("Message: ");
  for(int i = 0; i < length; i ++)
  {
    Serial.print(char(payload[i]));
  }
 
  // Print a newline
  Serial.println("");
}
