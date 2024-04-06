#!/usr/bin/env python
"""
This file houses all of the dumping functionality

@created: 3-22-2022
"""

import time
import sys

from roboclaw import Roboclaw

class Dumping:

    #---------------------------------------------------------------------
    # Dumping initialization function
    #
    # Establish the roboclaw connection for the bucket's linear actuator
    #---------------------------------------------------------------------
    def __init__(self, rc_port):
        try:
            print("Searching for dumping roboclaw, this may take a few seconds...")
            self.port = rc_port     #device port of roboclaw
            self.roboclaw = Roboclaw(self.port, 38400)
            self.roboclaw.Open()
            print("Dumping roboclaw connected successfully")
        except:
            print("Unable to find dumping roboclaw")

    #--------------------------------------------------------------------
    # Extend the bucket linear actuator
    #--------------------------------------------------------------------
    def bucket_extend(self, speed=100):
        if self.roboclaw != None:
            self.roboclaw.ForwardM1(128, 80)    #CHANGE THIS back to speed when mechanicals reinforce bucket

    #--------------------------------------------------------------------
    # Retract the bucket linear actuator
    #--------------------------------------------------------------------
    def bucket_retract(self, speed=-100):
        if self.roboclaw != None:
            self.roboclaw.BackwardM1(128, -80)  #CHANGE THIS back to speed when mechanicals reinforce bucket

    #--------------------------------------------------------------------
    # Stop the linear actuator
    #--------------------------------------------------------------------
    def bucket_stop(self):
        if self.roboclaw != None:
            self.roboclaw.ForwardM1(128, 0)

    #--------------------------------------------------------------------
    # A full dump algorithm
    #--------------------------------------------------------------------
    def full_dump(self, speed=127):
        self.bucket_extend(speed)
        time.sleep(10)
        self.bucket_retract(speed)
        time.sleep(10)

    #--------------------------------------------------------------------
    # Enables the roboclaw to communicate on the ACM# port
    #--------------------------------------------------------------------
    def enable_roboclaw(self):
        self.roboclaw = Roboclaw(self.port, 38400)
        self.roboclaw.Open()

    #--------------------------------------------------------------------
    # Disables the roboclaw to communicate on the ACM# port
    #--------------------------------------------------------------------
    def disable_roboclaw(self):
        self.bucket_stop()
        
        time.sleep(0.1)
