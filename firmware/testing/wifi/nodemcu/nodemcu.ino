#include <SoftwareSerial.h>
#include <ArduinoJson.h>

SoftwareSerial nodemcu(D6, D5); // RX, TX

void setup() {  
  Serial.begin(9600);
  nodemcu.begin(9600);
  while (!Serial) continue;
}

void loop()
{
    StaticJsonBuffer<1000> jsonBuffer;
    JsonObject& data = jsonBuffer.parseObject(nodemcu);

    if (data == JsonObject::invalid()) {
        Serial.println("Invalid JSON");
        jsonBuffer.clear();
        return;
    }

    Serial.println("JSON Object Recieved:");
    String first = data["test1"];
    Serial.println(first);
    String second = data["test2"];
    Serial.println(second);
    Serial.println("-----------------------------------------");
}