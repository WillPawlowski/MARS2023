#include "Adafruit_VL53L0X.h"
#include <Adafruit_ICM20X.h>
#include <Adafruit_ICM20948.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_VL53L0X depth_sensor = Adafruit_VL53L0X();
Adafruit_ICM20948 icm;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while(!Serial)
    delay(10);

  if(!icm.begin_I2C(0x68))
  {
    Serial.println("Failed to find ICM20948 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("ICM20948 Found!");

  if (!depth_sensor.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  Serial.println("VL53L0X Found!");
}

void loop() {
  // put your main code here, to run repeatedly:
  VL53L0X_RangingMeasurementData_t measure;
  depth_sensor.rangingTest(&measure, false);

  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t mag;
  sensors_event_t temp;
  icm.getEvent(&accel, &gyro, &temp, &mag);

  if (measure.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print("Distance (mm): "); Serial.println(measure.RangeMilliMeter);
  } else {
    Serial.println(" out of range ");
  }

  Serial.print("\t\tAccel X: ");
  Serial.print(accel.acceleration.x);
  Serial.print(" \tY: ");
  Serial.print(accel.acceleration.y);
  Serial.print(" \tZ: ");
  Serial.print(accel.acceleration.z);
  Serial.println(" m/s^2 ");

  delay(1000);

}
