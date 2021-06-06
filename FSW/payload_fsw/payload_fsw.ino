#include <Wire.h>
#include <EEPROM.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#include "Library.h"
#include "EEPROMManager.h"
#include "Sensors.h"

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#include <Adafruit_LSM6DS33.h>


// For SPI mode, we need a CS pin
#define LSM_CS 10
// For software-SPI mode we need SCK/MOSI/MISO pins
#define LSM_SCK 13
#define LSM_MISO 12
#define LSM_MOSI 11

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI
Adafruit_LSM6DS33 sox;
unsigned long delayTime;
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
float voltage_reading;
unsigned long mission_time;
int mission_state;
int address = 2;
int count = 0;
//const int led_pin 15;
int packetCount = 0;

void writeEEPROM_state() {
  EEPROM.update(address, mission_state);
  /*
  address = address + 1;
  if(address == EEPROM.length()) {
    address = 0;
  }
  */
}

void writeEEPROM_time() {
  if(mission_time < 255) {
    EEPROM.update(address, mission_time/100); // writes seconds value
  } else {
    count++;
    EEPROM.update(address + count, mission_time/100); // writes seconds value
  }
   
}

void writeEEPROM_pkt() {
  EEPROM.update(1, packetCount);
}

void readEEPROM_pkt() {
  packetCount = EEPROM.read(1);
}

void readEEPROM_state() {
  mission_state = EEPROM.read(0);
}

void readEEPROM_time() {
  mission_time = EEPROM.read(2 + count);
}

// creates and send telemetry packet to container over Serial.
// also saves it to SD card
void createDataPacket(sensors_event_t gyro) {
  // creating packet...
  packetCount++;
  String telemetryPacket = "3226,";
  telemetryPacket.concat(String(mission_time));
  telemetryPacket.concat(",");
  telemetryPacket.concat(String(packetCount));
  telemetryPacket.concat(",");
  telemetryPacket.concat("S1"); // this will be different for payload 2
  telemetryPacket.concat(",");
  telemetryPacket.concat(String(bme.readAltitude(SEALEVELPRESSURE_HPA)));
  telemetryPacket.concat(",");
  telemetryPacket.concat(String(bme.readTemperature()));
  // convert gyro z axis to RPM from radian/s, double check math
  telemetryPacket.concat(String(gyro.gyro.z * 60 / (2*3.14159)));
  telemetryPacket.concat("\n"); // newline will be the delimiter for packet
  
  // TODO: save packet to onboard sd card

  // send packet to container over Serial3 if it is available
  if(Serial3)
    Serial3.print(telemetryPacket);
}

void XBeeComsOut() {
  
}

void XBeeComsIn() {
  
}


void readVoltage() {
  int volt_val = analogRead(0); // place holder pin number
  float vout = (volt_val * 5.0) / 1024.0;
  float vin = vout / (100000.0 / (1000000.0 + 100000.0));
  voltage_reading = vin;
}

void setup() { // setup/recovery state
  // put your setup code here, to run once:

/* test to see what the init EEPROM values are
  readEEPROM_state();       
  readEEPROM_time();
  readEEPROM_pkt();
  */
  
  mission_state = 0;
  v0 = 0.0;
  alt = 0.0;
  Serial.begin(9600);
  Serial3.begin(9600); // Serial2 is the xbee, may need to change
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
    
    Serial.println("-- Setup function running --");
    delayTime = 1000;

    Serial.println();
  
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit LSM6DSOX test!");

  if (!sox.begin_I2C()) {
    // if (!sox.begin_SPI(LSM_CS)) {
    // if (!sox.begin_SPI(LSM_CS, LSM_SCK, LSM_MISO, LSM_MOSI)) {
    // Serial.println("Failed to find LSM6DSOX chip");
    while (1) {
      delay(10);
    }
  }

    sox.getAccelRange();

    sox.getGyroRange();

    sox.getAccelDataRate();

    sox.getGyroDataRate();

    
}

void loop() {
  // put your main code here, to run repeatedly:
  mission_time = millis(); // getting the mission time in millieconds
  writeEEPROM_time();
  readVoltage();
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;

  
  
  sox.getEvent(&accel, &gyro, &temp);

  accel_val = sqrt(pow(accel.acceleration.x, 2) + pow(accel.acceleration.y, 2) + pow(accel.acceleration.z, 2));

  // print out the acceleration values
  Serial.print("\t\tAccel X: ");
  Serial.print(accel.acceleration.x);
  Serial.print(" \tY: ");
  Serial.print(accel.acceleration.y);
  Serial.print(" \tZ: ");
  Serial.print(accel.acceleration.z);
  Serial.println(" m/s^2 ");

  // print out the gyro values
  Serial.print("\t\tGyro X: ");
  Serial.print(gyro.gyro.x);
  Serial.print(" \tY: ");
  Serial.print(gyro.gyro.y);
  Serial.print(" \tZ: ");
  Serial.print(gyro.gyro.z);
  Serial.println(" radians/s ");
  Serial.println();

  // Bme 280 readings
  Serial.print("Temperature = ");
  Serial.print(bme.readTemperature());
  Serial.println(" °C");

  alt = bme.readAltitude(SEALEVELPRESSURE_HPA));
  Serial.print("Approx. Altitude = ");
  Serial.print(alt);
  Serial.println(" m");

  Serial.print("Humidity = ");
  Serial.print(bme.readHumidity());
  Serial.println(" %");
  
  v = v0 + accel_val*time_in_flight; // 


  
  // TODO: save packet to onboard sd card
  writeEEPROM_pkt();

  // state switch statement 
  if(v >= 5.00) { // launchpad -> ascent state (read + trans)
    mission_state = 2;
    writeEEPROM_state();
    createDataPacket(gyro);
    
  } else if (v < 0.0 && alt > 670) { // ascent -> descent state (read + trans)
    mission_state = 3;
    writeEEPROM_state();
    createDataPacket(gyro);

  } else { // lauchpad state (read + trans)
    mission_state = 1;
    writeEEPROM_state();
    createDataPacket(gyro);
    
  }

}
