import rospy
from std_msgs.msg import Int32

from locomotion import Locomotion

class locomotionWrapperROS:

    def __init__(self):
        self.locomotion = Locomotion()

        self.opcode = -1

        rospy.Subscriber("main_manual", Int32, self.callback_main)
        rospy.Subscriber("emergency_stop", Int32, self.callback_stop)

    def callback_main(self, msg):
        self.opcode = msg.data

        if self.opcode >= 0 and self.opcode <= 6:
            if self.opcode == 0:
                self.locomotion.loco_forward()
            if self.opcode == 1:
                self.locomotion.loco_left()
            if self.opcode == 2:
                self.locomotion.loco_backwards()
            if self.opcode == 3:
                self.locomotion.loco_right()
            if self.opcode == 4:
                self.locomotion.loco_stop()
            if self.opdcode == 5:
                self.locomotion.loco_engage_motors()
            if self.opdcode == 6:
                self.locomotion.loco_disengage_motors()


    def callback_stop(self, msg):
        self.opcode = msg.data

        if self.opcode == 1:
            try:
                self.stop()
                print(self.opcode)
                print("Successfully shutdown the Locomotion subsystem.")
            except:
                print("Something went wrong with Locomotion shutdown.")
        elif self.opcode == 2:
            self.locomotion.loco_engage_motors()

    def stop(self):
        self.locomotion.loco_disengage_motors()

if __name__ == "__main__":
    rospy.init_node("locomotion_node")

    locomotion_wrapper = locomotionWrapperROS()

    rospy.on_shutdown(locomotion_wrapper.stop)

    rospy.loginfo("Locomotion node initialized successfully.")

    rospy.spin()
