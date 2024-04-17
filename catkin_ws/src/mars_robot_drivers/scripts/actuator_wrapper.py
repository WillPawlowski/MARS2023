#!/usr/bin/env python

"""
This script is used to perform start a roboclaw actuator node to perform actuator operations manually
"""

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

from actuator_driver import Actuator

class Actuator_WrapperROS:

    def __init__(self):
        rc_port = rospy.get_param('/mars_robot/ports/roboclaw_port')    #device port of roboclaw

        self.actuator = Actuator(rc_port)
        
        self.bucket_speed = rospy.get_param('mars_robot/motor_speeds/bucket_speed')
        self.tool_speed = rospy.get_param('mars_robot/motor_speeds/tool_speed')

        rospy.Subscriber("main_control", String, self.callback_main)
    
    def callback_main(self, msg):
        opcode = msg.data

        #Bucket actuator commands
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/bucket_extend_key'):
            self.actuator.bucket_extend(self.bucket_speed)
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/bucket_stop_key'):
            self.actuator.bucket_stop()
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/bucket_retract_key'):
            self.actuator.bucket_retract(self.bucket_speed)
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/bucket_cycle_key'):
            self.actuator.full_bucket_cycle()

        #Tool actuator commands
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/tool_extend_key'):
            self.actuator.tool_extend(self.tool_speed)
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/tool_stop_key'):
            self.actuator.tool_stop() 
        if opcode == rospy.get_param('/mars_robot/manual_control_keys/tool_retract_key'):
            self.actuator.tool_retract(self.tool_speed) 
                
    def stop(self):
        self.actuator.disable_roboclaw()
    
    def engage(self):
        self.actuator.enable_roboclaw()

if __name__ == "__main__":
    rospy.init_node("dumping_node")

    actuator_wrapper = Actuator_WrapperROS()

    rospy.on_shutdown(actuator_wrapper.stop)

    rospy.loginfo("Roboclaw actuator node initialized successfully")

    rospy.spin()
