#!/usr/bin/env python

from AR_week4_test.srv import compute_cubic_traj,compute_cubic_trajResponse
import rospy
import numpy as np

def compute_traj(req):
    print ("hello")
    #calculate the values of coeffs recievd on the service
    v0=req.v0
    vf=req.vf
    p0=req.p0
    pf=req.pf
    t0=req.t0
    tf=req.tf
    m=np.array([[1, t0 , t0*t0, t0*t0*t0], [0,  1 , t0*2,  3*t0*t0] ,[1,  tf,  tf*tf,  tf*tf*tf], [0,  1,  tf*2,  tf*tf*3]])
    ps=np.array([[p0],[v0],[pf],[vf]])
    #multiplication of inverse matrix and c matrix
    x=np.linalg.inv(m).dot(ps)
    #transpose the matrix to get the value of coefficients on the first row
    x=np.transpose(x)
    #return the computed coeffciens via service back to node 3
    return compute_cubic_trajResponse(x[0][0],x[0][1],x[0][2],x[0][3])
def compute_cubic_server():
    rospy.init_node('compute_cubic_server')
    s = rospy.Service('cubic_trajectory',compute_cubic_traj,compute_traj)
    print "Ready to compute coeffs"
    rospy.spin()
    #rospy.spin() doesnt allow it to sleep until terminated

if __name__ == "__main__":
    compute_cubic_server()
