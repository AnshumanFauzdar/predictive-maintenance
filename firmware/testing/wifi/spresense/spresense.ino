#include <SoftwareSerial.h>
#include <ArduinoJson.h>

SoftwareSerial nodemcu(0, 1); // RX, TX

void setup() {
  Serial.begin(9600);
  nodemcu.begin(9600);
  delay(1000);
  Serial.println("Test Started");
}

void loop()
{
    // Start JSON data
    StaticJsonBuffer<1000> jsonBuffer;
    JsonObject& data = jsonBuffer.createObject();

    // Add values to JSON data
    data["test1"] = "ok";
    data["test2"] = "working";

    // Send JSON data to nodeMCU

    data.printTo(nodemcu);
    jsonBuffer.clear();
    delay(2000);
}