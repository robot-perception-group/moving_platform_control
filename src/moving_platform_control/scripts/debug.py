#!/usr/bin/python

import rospy
from uav_msgs.msg import uav_pose
from librepilot.msg import LibrepilotActuators



node_name = 'debug_node'
moving_platform_name = rospy.get_param(rospy.get_namespace()+node_name+'/mp_name','moving_platform')  
publish_hz = float(rospy.get_param(rospy.get_namespace()+node_name+'/publish_hz','10'))
actuator_topic = ('actuatorcommand',LibrepilotActuators)
uav_pose_topic = ('command',uav_pose)

class Debug():
    def __init__(self):
        self.actuator_publisher = rospy.Publisher(actuator_topic[0],actuator_topic[1],queue_size = 1)
        self.uav_pose_publisher = rospy.Publisher(uav_pose_topic[0],uav_pose_topic[1],queue_size = 1)
        self.test_values = [1611,1622,1633,1644,0,1,2,3,4,5,6,7]

    def send_msg(self):
        msg_actuatorcommand = LibrepilotActuators()
        msg_actuatorcommand.data.data = self.test_values
        self.actuator_publisher.publish(msg_actuatorcommand)
        msg_command = uav_pose()
        msg_command.flightmode = 3
        self.uav_pose_publisher.publish(msg_command)
        return


if __name__ == '__main__':
    rospy.init_node('debug_node')
    debug = Debug()
    rate = rospy.Rate(publish_hz)
    while not rospy.is_shutdown():
        debug.send_msg()
        rate.sleep()



