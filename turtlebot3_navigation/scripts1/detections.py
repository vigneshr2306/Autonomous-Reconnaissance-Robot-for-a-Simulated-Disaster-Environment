#!/usr/bin/env python3

import json	
import rospy
import tf
#from scipy.spatial.transform import Rotation as R
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Float64
from apriltag_ros.msg import AprilTagDetectionArray

def callback(data):

    dict_apriltag = {}
    while not rospy.is_shutdown():
        for i in range(len(data.detections)):   
            id = data.detections[i].id[0]
            dict_apriltag[id] = data.detections[i].pose.pose.pose
            
            tag_name = 'tag_' + str(id)
            print(tag_name)
            (trans, rot) = listener.lookupTransform(tag_name, '/map', rospy.Time(0))
            
            # r = R.as_matrix(rot)
            # r.as_quat()
            dict_apriltag[id] = (trans, rot)
        print(dict_apriltag)
    with open('convert.txt', 'w') as convert_file:
     	convert_file.write(json.dumps(dict_apriltag))

if __name__ == '__main__':
    rospy.init_node('Node', anonymous=True)
    listener = tf.TransformListener()
    
    while(True):
          
        sub = rospy.Subscriber("/tag_detections", AprilTagDetectionArray, callback)
