
#include "HyperDisplay_UG2856KLBAG01.h"   
#define SERIAL_PORT Serial  
#define SPI_PORT SPI  

#define RES_PIN 2          //Pin Assignment
#define CS_PIN 4          
#define DC_PIN 5           

// END USER SETUP

UG2856KLBAG01_SPI dispOLED;  // Declare a SPI-based Transparent dispOLED 

String val = "waiting";

void setup() {
  Serial.begin(9600);
  SPI_PORT.begin();
  dispOLED.begin(CS_PIN, DC_PIN, SPI_PORT);  //Assign pins to the display variable
}

void loop() {
  if(Serial.available()){
    val = Serial.readStringUntil('\n');
    dispOLED.windowClear();
    dispOLED.setWindowColorSet();
    dispOLED.setTextCursor(50,25);
    dispOLED.print(val);
    delay(500);
  } else{
    dispOLED.windowClear();
    dispOLED.setWindowColorSet();
    dispOLED.setTextCursor(60,25);
    dispOLED.print("waiting");
    delay(500);
    }
}
