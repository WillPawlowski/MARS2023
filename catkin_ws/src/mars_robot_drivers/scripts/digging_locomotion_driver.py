#!/usr/bin/env python3
"""
This file houses all of the digging and locomotion functionality
These two systems were combined into 1 script because we were continuosly
recvieving a "[USB] Could not claim interface � on USB device: -6" when 
trying to access odrives in seperate files.

@created: 3-22-2022
"""

import odrive
from odrive.utils import dump_errors
from odrive.enums import *
import subprocess
import yaml
import time

class Digging_Locomotion:
    #---------------------------------------------------------------------
    # Digging initialize function
    # 
    # Establish the odrive connection for auger
    #---------------------------------------------------------------------
    def __init__(self, odrv0_SN, pitch_SN):
    #def __init__(self, odrv0_SN):
        self.pitch_serial_num = pitch_SN
        self.odrv0_serial_num = odrv0_SN

        try:
            print("Searching for locomotion odrive, this may take a few seconds...")
            self.odrv1 = odrive.find_any(serial_number=self.odrv0_serial_num)
            print("Locomotion odrive connected successfully") 
        except:
            print("Unable to find locomotion odrive")

        self.pitch_motor_engage()
        self.loco_engage_motors()
        
    #---------------------------------------------------------------------
    # Helper function to operate the stepper motor from tic36v4
    # 
    # param: *args -- a variable set of arguments used to send commands
    #---------------------------------------------------------------------
    def ticcmd(self, *args):
        return subprocess.check_output(['ticcmd'] + list(args))

    def digging_motors_disengage(self):
        self.pitch_motor_disengage()

    ##====================================================================
    ##      PITCH MOTOR FUNCTIONS:
    ##====================================================================

    #---------------------------------------------------------------------
    # Starts the pitch motor by setting a velocity
    # param: speed [microsteps/100000 seconds] (max speed: [ENTER MAX HERE])
    #        + speed = [ENTER CW OR CCW HERE]
    #        - speed = [ENTER CCW OR CW HERE]
    #---------------------------------------------------------------------
    def pitch_motor_turn(self, speed):
        self.ticcmd('-d', self.pitch_serial_num, '--exit-safe-start', '-y', str(speed))

    #---------------------------------------------------------------------
    # Stops the pitch motor by setting speed to 0
    #---------------------------------------------------------------------
    def pitch_motor_stop(self):
        self.ticcmd('-d', self.pitch_serial_num, '--exit-safe-start', '-y', str(0))

    #---------------------------------------------------------------------
    # Engages the pitch motor by reseting zero position & resuming tic36v4
    #---------------------------------------------------------------------
    def pitch_motor_engage(self):
        self.ticcmd('-d', self.pitch_serial_num, '--reset')
        self.ticcmd('-d', self.pitch_serial_num, '--resume')

    #---------------------------------------------------------------------
    # Disengages the pitch motor by deenergizing the tic36v4
    #---------------------------------------------------------------------
    def pitch_motor_disengage(self):
        self.pitch_motor_stop()
        self.ticcmd('-d', self.pitch_serial_num, '--deenergize')

    #---------------------------------------------------------------------
    # Returns: the position estimation of the digging motor [microsteps]
    #---------------------------------------------------------------------
    def get_pitch_motor_pos(self):
        status = yaml.safe_load(self.ticcmd('-d', self.pitch_serial_num, '-s', '--full'))
        return status['Current position']

    #---------------------------------------------------------------------
    # Returns: the velocity estimation of the digging motor [microsteps/ 10000 seconds]
    #---------------------------------------------------------------------
    def get_pitch_motor_vel(self):
        status = yaml.safe_load(self.ticcmd('-d', self.pitch_serial_num, '-s', '--full'))
        return status['Current velocity']

    ##====================================================================
    ##      LOCOMOTION MOTOR FUNCTIONS:
    ##====================================================================

    #--------------------------------------------------------------------
    # Drives robot forward
    #
    # param: speed -- set the speed of movement (max at 67)
    #--------------------------------------------------------------------
    def loco_forward(self, left_speed, right_speed):
        self.odrv1.axis0.controller.input_vel = 0
        self.odrv1.axis1.controller.input_vel = 0

        time.sleep(0.1)

        self.odrv1.axis0.controller.input_vel = -left_speed
        self.odrv1.axis1.controller.input_vel = right_speed

    #--------------------------------------------------------------------
    # Zero point turn left
    #
    # param: speed -- set the speed of movement (max at 67)
    #--------------------------------------------------------------------
    def loco_left(self, left_speed, right_speed):
        self.odrv1.axis0.controller.input_vel = 0
        self.odrv1.axis1.controller.input_vel = 0

        time.sleep(0.1)

        self.odrv1.axis0.controller.input_vel = left_speed
        self.odrv1.axis1.controller.input_vel = -right_speed
    
    #--------------------------------------------------------------------
    # Drives robot in reverse
    #
    # param: speed -- sets the speed of movement (max at speed)
    #--------------------------------------------------------------------
    def loco_back(self, left_speed, right_speed):
        self.odrv1.axis0.controller.input_vel = 0
        self.odrv1.axis1.controller.input_vel = 0

        time.sleep(0.1)

        self.odrv1.axis0.controller.input_vel = left_speed
        self.odrv1.axis1.controller.input_vel = -right_speed

    #--------------------------------------------------------------------
    # Zero point turn right 
    #
    # param: speed -- sets the speed of movement (max at 50)
    #--------------------------------------------------------------------
    def loco_right(self, left_speed, right_speed):
        self.odrv1.axis0.controller.input_vel = 0
        self.odrv1.axis1.controller.input_vel = 0

        time.sleep(0.1)

        self.odrv1.axis0.controller.input_vel = -left_speed
        self.odrv1.axis1.controller.input_vel = right_speed
    
    #--------------------------------------------------------------------
    # Stops all movement
    # 
    # Stopping right to 0 causes ringing in the motor, so stopping is set
    # to the following: (speed) -> 0 -> 5 -> 0
    #--------------------------------------------------------------------
    def loco_stop(self):
        self.odrv1.axis0.controller.input_vel = 0
        self.odrv1.axis1.controller.input_vel = 0

        time.sleep(0.1)

        self.odrv1.axis0.controller.input_vel = -5
        self.odrv1.axis1.controller.input_vel = 5

        time.sleep(0.1)

        self.odrv1.axis0.controller.input_vel = 0
        self.odrv1.axis1.controller.input_vel = 0

    #--------------------------------------------------------------------
    # Engages the locomotion motors by setting their state and control mode (velocity)
    #--------------------------------------------------------------------
    def loco_engage_motors(self):
        self.odrv1.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.odrv1.axis0.controller.config.control_mode = 2 #Velocity control
        self.odrv1.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.odrv1.axis1.controller.config.control_mode = 2 #Velocity control

    #--------------------------------------------------------------------
    # Disengages the locomotion motors by setting their state
    #--------------------------------------------------------------------
    def loco_disengage_motors(self):
        self.loco_stop()

        time.sleep(0.1)

        self.odrv1.axis0.requested_state = AXIS_STATE_IDLE
        self.odrv1.axis1.requested_state = AXIS_STATE_IDLE

    #---------------------------------------------------------------------
    # Returns: the current of the loco motor
    #
    # motor.current_control.Iq_setpoint is commanded current 
    # motor.current_control.Iq_measured is measured motor current
    #   Odrive reference states setpoint value is less noisy and still accurate 
    #   unless motor is near max rpm
    #---------------------------------------------------------------------
    def get_left_loco_motor_current(self):
        return self.odrv1.axis0.motor.current_control.Iq_measured

    def get_right_loco_motor_current(self):
        return self.odrv1.axis1.motor.current_control.Iq_measured
    
    #---------------------------------------------------------------------
    # Returns: the position estimation of the loco motor [turns]
    #---------------------------------------------------------------------
    def get_left_loco_motor_pos(self):
        return self.odrv1.axis0.encoder.pos_estimate

    def get_right_loco_motor_pos(self):
        return self.odrv1.axis1.encoder.pos_estimate
    
    #---------------------------------------------------------------------
    # Returns: the velocity estimation of the auger motor [turns/s]
    #---------------------------------------------------------------------
    def get_left_loco_motor_vel(self):
        return self.odrv1.axis0.encoder.vel_estimate
    
    def get_right_loco_motor_vel(self):
        return self.odrv1.axis1.encoder.vel_estimate    

    #--------------------------------------------------------------------
    # Dumps all errors from the locomotion odrive
    #--------------------------------------------------------------------
    def loco_dump_errors(self):
        dump_errors(self.odrv1, True)
