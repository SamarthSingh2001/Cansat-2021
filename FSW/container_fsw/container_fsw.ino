#include <Adafruit_GPS.h>
#include <XBee.h> // for xbee library stuff, https://www.arduino.cc/reference/en/libraries/xbee-arduino-library/
// TODO: double check the library is usable/compatible with XBee pro 900HP 

// what's the name of the hardware serial port?
#define GPSSerial Serial

// Connect to the GPS on the hardware port
Adafruit_GPS GPS(&GPSSerial);

// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences
#define GPSECHO false

uint32_t timer = millis();

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI

unsigned long delayTime;
float temp_data;
float pres_data;
float alt_data;
float hum_data;
float temperature;
float a_x;
float a_y;
float a_z;
float gyro_x;
float gyro_y;
float gyro_z;
float v0;
float time_in_flight;
float v;
float accel_val;
float alt;

const int LEDpin = 15;
const int BUZZERpin = 16;

//#include <NewSoftSerial.h>
// For the electronic wiring , you should :
// Connect pinRx to the Pin2 of XBee(Tx , Dout)
// Connect pinTx to the Pin3 of XBee(Rx , Din)

// Define the pins on Arduino for XBee comminication
uint8_t pinRx = 2 , pinTx = 4; // the pin on Arduino
long BaudRate = 57600 , sysTick = 0;
char GotChar;
// Initialize NewSoftSerial
//NewSoftSerial mySerial( pinRx , pinTx );
XBee xbeePayload = XBee();
XBee xbeeGS = XBee();

// FIXME: i think these should be SH/SL, not 0 or 1 or 4
#define XBEE_SP1_DEST_ADDR  0x0000 // 0
#define XBEE_SP2_DEST_ADDR  0x0001 // 1
#define XBEE_GS_DEST_ADDR   0x0100 // 4

void XBeeCommsOut() {
  
}

void XBeeCommsIn() {
  
}


void setup() {
  pinMode(LEDpin, OUTPUT);
  pinMode(BUZZERpin, OUTPUT);
  // put your setup code here, to run once:
  //while (!Serial);  // uncomment to have the sketch wait until Serial is ready

  // connect at 115200 so we can read the GPS fast enough and echo without dropping chars
  // also spit it out
  Serial.begin(115200);
  Serial.println("Adafruit GPS library basic parsing test!");

  // 9600 NMEA is the default baud rate for Adafruit MTK GPS's- some use 4800
  GPS.begin(9600);
  // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // uncomment this line to turn on only the "minimum recommended" data
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  // For parsing data, we don't suggest using anything but either RMC only or RMC+GGA since
  // the parser doesn't care about other sentences at this time
  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // 1 Hz update rate
  // For the parsing code to work nicely and have time to sort thru the data, and
  // print it out we don't suggest using anything higher than 1 Hz

  // Request updates on antenna status, comment out to keep quiet
  GPS.sendCommand(PGCMD_ANTENNA);

  delay(1000);

  // Ask for firmware version
  GPSSerial.println(PMTK_Q_RELEASE);
  while(!Serial);    // time to get serial running
    Serial.println(F("BME280 test"));

    unsigned status;
    
    // default settings
    status = bme.begin();  
    // You can also pass in a Wire library object like &Wire2
    // status = bme.begin(0x76, &Wire2)
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1) delay(10);
    }
    
    Serial.println("-- Default Test --");
    delayTime = 1000;

    Serial.println();
 /* Serial.begin(BaudRate);
  Serial.println("XBee Communication Test Start !");
  Serial.print("BaudRate:");
  Serial.println(BaudRate);
  Serial.print("NewSoftSerial Rx Pin#");
  Serial.println(pinRx,DEC);
  Serial.print("NewSoftSerial Tx Pin#");
  Serial.println(pinTx,DEC); */

  // This part is the NewSoftSerial for talking to XBee
  //mySerial.begin(BaudRate);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  xbeePayload.readPacket();
  xbeeGS.readPacket();
  // reference https://github.com/andrewrapp/xbee-arduino/blob/master/examples/Series1_Rx/Series1_Rx.pde
  // for receiving packets
  // do stuff if a response is available
  if(xbeePayload.getResponse().isAvailable()){

  }

  char c = GPS.read();
  if(GPS.fix) { // get the gps information
      Serial.print("Location: ");
      Serial.print(GPS.latitude, 4); Serial.print(GPS.lat);
      Serial.print(", ");
      Serial.print(GPS.longitude, 4); Serial.println(GPS.lon);
      Serial.print("Speed (knots): "); Serial.println(GPS.speed);
      Serial.print("Angle: "); Serial.println(GPS.angle);
      Serial.print("Altitude: "); Serial.println(GPS.altitude);
      Serial.print("Satellites: "); Serial.println((int)GPS.satellites);
  }
  temp_data = bme.readTemperature(); // reading the temperature
  pres_data = bme.readPressure();
  alt_data = bme.readAltitude(SEALEVELPRESSURE_HPA);
  hum_data = bme.readHumidity();

  if(v > 5.0) { // launchpad -> ascent (read/transmit to GCS)
    
  } else if(v < 0.0 && alt >= 670) { // ascent -> descent (read/transmit to GCS)
    
  } else if(alt = 0.0 && v == 0.0) { // descent -> landed (collect telem from SP, read and transmit, release of payloads)
    if(alt == 500) { // release SP1
      
    } else if (alt == 400) { // release SP2
      
    } else if(alt <= 0.0) {
      digitalWrite(LEDpin, HIGH);
      digitalWrite(BUZZERpin, HIGH);
    }
  } else { // launchpad (read/transmit to GCS)
    
  }
  
}
