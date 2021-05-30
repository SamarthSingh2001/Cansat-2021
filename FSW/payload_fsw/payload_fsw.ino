#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#include <Adafruit_LSM6DSOX.h>


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
Adafruit_LSM6DSOX sox;
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

void setup() { // setup/recovery state
  // put your setup code here, to run once:
  v0 = 0.0;
  Serial.begin(9600);
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
  
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;

  sox.getEvent(&accel, &gyro, &temp);

  accel_val = sqrt(pow(accel.acceleration.x, 2) + pow(accel.acceleration.y, 2) + pow(accel.acceleration.z, 2));
  
  v = v0 + accel_val*time_in_flight;

  // state switch statement bullshit
  if(v >= 5.00) { // launchpad -> ascent state (read + trans)
    
  } else if (v < 0.0 && alt > 670) { // ascent -> descent state (read + trans)
    
  } else { // lauchpad state (read + trans)
    
  }

}
