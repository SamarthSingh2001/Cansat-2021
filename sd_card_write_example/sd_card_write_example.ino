#include <SPI.h>
#include <SD.h>

#ifndef SDCARD_SS_PIN
const uint8_t SD_CS_PIN = SS;
#else  // SDCARD_SS_PIN
// Assume built-in SD is used.
const uint8_t SD_CS_PIN = SDCARD_SS_PIN;
#endif  // SDCARD_SS_PIN

File myFile;

void writeSDCard() {
  if(myFile) {
    myFile.println("data"); // this is how you write
    myFile.close();
  }
}

void readSDCard() {
  if(myFile) {
    while(myFile.available()) {
      Serial.write(myFile.read());
    }
    myFile.close();
  }
}



void setup() {
 
  Serial.begin(9600);
  
  while(!Serial) {
    ;
  }
  

  if(!SD.begin(4)) { // this may need to be changed
    Serial.println("SD init failed");
    while(1);
  }

  // write to a file
  myFile = SD.open("example.txt", FILE_WRITE);
  writeSDCard();

  // read from it
  myFile = SD.open("example.txt");
  readSDCard();
}
