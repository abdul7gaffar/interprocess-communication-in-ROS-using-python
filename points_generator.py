#!/usr/bin/env python

import rospy
import random
from AR_week4_test.msg import cubic_traj_params

def node1():
    pub = rospy.Publisher('chatter', cubic_traj_params, queue_size=10) # to create a topic to publish the randomly genrated poitns on
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(0.05) #  to give a delay of 20 seconds 
    while not rospy.is_shutdown():
	# random point generation
       	v0=random.uniform(-10,10)
	vf=random.uniform(-10,10)
	p0=random.uniform(-10,10)
	pf=random.uniform(-10,10)
	t0=0
	dt=random.uniform(5,10)
	tf=t0+dt
	params=cubic_traj_params()#create params of message type cubic_traj_params
	#assign values to the each attribute in the created message type to pass
	params.p0=p0
	params.pf=pf
	params.v0=v0
	params.vf=vf
	params.t0=t0
	params.tf=tf	
        rospy.loginfo(params) #creates a log info
        pub.publish(params)#publish it on the created topic
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
