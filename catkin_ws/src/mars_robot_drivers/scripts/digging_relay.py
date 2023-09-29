#!/usr/bin/env python
import rospy
import math
from mars_robot_msgs.msg import sensor_msg
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from time import sleep

pub = rospy.Publisher('main_control',String,queue_size = 1)
depth_extending = False
pitch_up = True
publish_data = 'i'
#f = open("sensor_data_3-18.txt", "w")

MAX_DEPTH = 300
MIN_DEPTH = 200
AUGER_TOTAL_LENGTH = 773 #measurement in mm, distance from top gearbox to end of 
SHAFT_2_GROUND = 260 #measurement in mm, distance from bottom of treads to auger's rotational shaft
SENSOR_2_SHAFT = 110 #measurement in mm, distance from distanct sensor to auger's rotational shaft

depth_increase_key = 'o'#rospy.get_param('/mars_robot/manual_control_keys/depth_increase_slow_key')
depth_decrease_key = 'u'#rospy.get_param('/mars_robot/manual_control_keys/depth_decrease_slow_key')
pitch_increase_fast_key = 'h'
pitch_increase_slow_key = 'j'
pitch_stop = 'k'
pitch_decrease_slow_key = 'l'



#should loop between increasing and decreasing depth
def callback(sensor_msg):
    #print("Received Data\n")

    global publish_data

    #Variables for data
    depth_reading = sensor_msg.data[0]
    auger_accel_z = sensor_msg.data[1]
    if auger_accel_z == 0:
        auger_accel_z = 0.01
    auger_accel_x = sensor_msg.data[2]
    
    #Derived Measurements
    #Distance from the distance sensor to the bottom of the auger
    auger_ext_length = AUGER_TOTAL_LENGTH - depth_reading
    #Angle of the auger relative to the ground/gravity
    pitch_angle = math.pi/2 + math.atan(auger_accel_x/auger_accel_z)
    pitch_angle_deg = pitch_angle*180/math.pi #degrees
    

    #angle of auger connector relative to ground
    theta = math.pi/2-pitch_angle

    #sin values of above angles
    sin_pitch = math.sin(pitch_angle)
    sin_theta = math.sin(theta)

    sensor_2_ground = sin_theta*SENSOR_2_SHAFT + SHAFT_2_GROUND
    auger_depth_from_sensor = sin_pitch*auger_ext_length
    auger_depth = auger_depth_from_sensor - sensor_2_ground
    
    f = open("pitch_angle.txt","w")
    f.write("X accel: ")
    f.write(str(auger_accel_x))
    f.write("\n")
    f.write("Z accel: ")
    f.write(str(auger_accel_z))
    f.write("\n")
    f.write("Angle: ")
    f.write(str(pitch_angle))
    f.write("\n\n")

    print("Dist Reading: ")
    print(depth_reading)
    print("\n")
    print("Auger Angle: ")
    print(pitch_angle_deg)
    print("\n")
    print("Auger Depth: ")
    print(str(auger_depth))

    print("\n========================\n")

   # if(pitch_angle_deg < 45):
#	publish_data = pitch_increase_slow_key
#	pub.publish(publish_data)
#	sleep(1)
#	publish_data = pitch_stop
#	pub.publish(publish_data)
#	sleep(1)
 #   elif(pitch_angle_deg < 50):
  #      print("Set key to increase pitch\n")
   #     publish_data = pitch_increase_slow_key
#	pub.publish(publish_data)
#	sleep(1)
#	publish_data = pitch_stop
#	pub.publish(publish_data)
#	sleep(1)
	#elif(depth_reading <= MIN_DEPTH and publish_data != depth_decrease_key):
     #   print("Set key to decrease depth\n")
        #publish_data = depth_decrease_key


    #print("==============================================\n")
    #f.write("Depth: ")
    #f.write(str(depth_reading)
   # f.write("\n")
    sleep(0.5)

def subscriber():
    rospy.Subscriber('sensor_data', Float32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    #f = open("sensor_data_3-18.txt", "w")
    f = open("pitch_angle", "w")
    rospy.init_node('digging_relay_node')
    subscriber()

