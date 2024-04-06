#!/usr/bin/env python
"""
This file houses all of the tool functionality

@created: 4-6-2024
"""

import time
import sys

from roboclaw import Roboclaw

class Tool:

    #---------------------------------------------------------------------
    # Tool initialization function
    #
    # Establish the roboclaw connection for the tool's linear actuator
    #---------------------------------------------------------------------
    def __init__(self, rc_port):
        try:
            print("Searching for tool roboclaw, this may take a few seconds...")
            self.port = rc_port     #device port of roboclaw
            self.roboclaw = Roboclaw(self.port, 38400)
            self.roboclaw.Open()
            print("Tool roboclaw connected successfully")
        except:
            print("Unable to find tool roboclaw")

    #--------------------------------------------------------------------
    # Extend the  tool's linear actuator
    #--------------------------------------------------------------------
    def tool_extend(self, speed=100):
        if self.roboclaw != None:
            self.roboclaw.ForwardM2(128, 80)    #CHANGE THIS back to speed when mechanicals reinforce bucket

    #--------------------------------------------------------------------
    # Retract the tool's linear actuator
    #--------------------------------------------------------------------
    def tool_retract(self, speed=-100):
        if self.roboclaw != None:
            self.roboclaw.BackwardM2(128, -80)  #CHANGE THIS back to speed when mechanicals reinforce bucket

    #--------------------------------------------------------------------
    # Stop the tool's linear actuator
    #--------------------------------------------------------------------
    def tool_stop(self):
        if self.roboclaw != None:
            self.roboclaw.ForwardM2(128, 0)

    #--------------------------------------------------------------------
    # Enables the roboclaw to communicate on the ACM# port
    #--------------------------------------------------------------------
    def enable_tool_roboclaw(self):
        self.roboclaw = Roboclaw(self.port, 38400)
        self.roboclaw.Open()

    #--------------------------------------------------------------------
    # Disables the roboclaw to communicate on the ACM# port
    #--------------------------------------------------------------------
    def disable_tool_roboclaw(self):
        self.tool_stop()
        
        time.sleep(0.1)
