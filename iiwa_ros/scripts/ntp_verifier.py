#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from iiwa_msgs.msg import CartesianPose

rospy.init_node('ntp_verifier')
rate = rospy.Rate(5)

last_msg = None
diff = None

def ntplog(msg):
    global last_msg, diff
    diff = msg.poseStamped.header.stamp - rospy.Time.now()
    diff = round(diff.to_sec(), 6)
    last_msg = msg


sub = rospy.Subscriber('/iiwa/state/CartesianPose', CartesianPose, ntplog, queue_size=1)

while not rospy.is_shutdown():
    rospy.loginfo(f'The current time difference is: {diff} secs')
    rate.sleep()
