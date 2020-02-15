#!/usr/bin/env python
from std_msgs.msg import Float32
import rospy
from AR_week4_test.msg import cubic_traj_params,cubic_traj_coeffs
from AR_week4_test.srv import *

def node4():
    rospy.init_node('node4', anonymous=True)

    rospy.Subscriber('tonode4',cubic_traj_coeffs, callback1)
    rospy.spin()
def callback1(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s',data)
 #extract the coefficients and intial time and final time
 a0=data.a0
 a1=data.a1
 a2=data.a2
 a3=data.a3
 t0=data.t0
 tf=data.tf
 print(data)
 t=0
 while t<tf:
	#calculate the postion, accelaration and speed trajectory
	position=a0+(a1*t)+(a2*t*t)+(a3*t*t*t)
	speed=a1+(a2*2*t)+(a3*3*t*t)
	acc=a2*2+(a3*6*t)
	# send it to talker to publish it on a new topic each
	talker(position,speed,acc)
	t=t+0.001
def talker(position,speed,acc):
    #create three new topics to publish three new trajectories
    pub=rospy.Publisher('position_traj',Float32, queue_size=10)
    pub1=rospy.Publisher('speed_traj',Float32, queue_size=10)
    pub2=rospy.Publisher('acc_traj',Float32, queue_size=10)
    pub.publish(position)
    pub1.publish(speed)
    pub2.publish(acc)
if __name__ == '__main__':
    node4()
