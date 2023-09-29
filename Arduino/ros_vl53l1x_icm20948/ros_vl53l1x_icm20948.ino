
#include <ros.h>

#include "Adafruit_VL53L0X.h"
#include <Adafruit_ICM20X.h>
#include <Adafruit_ICM20948.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <mars_robot_msgs/sensor_msg.h>
ros::NodeHandle nh;

Adafruit_VL53L0X depth_sensor = Adafruit_VL53L0X();
Adafruit_ICM20948 icm;
mars_robot_msgs::sensor_msg sensormsg_msg;
ros::Publisher sensor_data("sensor_data", &sensormsg_msg);

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

  nh.initNode();
  nh.advertise(sensor_data);

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

  sensormsg_msg.auger_depth = measure.RangeMilliMeter;
  sensormsg_msg.auger_accel_z = accel.acceleration.z;
  sensormsg_msg.auger_accel_x = accel.acceleration.x;

  sensor_data.publish( &sensormsg_msg);
  nh.spinOnce();
  delay(1000);

}
