# Project_Donatello
# Members: Vignesh Ravikumar, Skanda Akkihebbal Prasanna, Pavan Rathnakar Shetty, Santhosh Sankar, Aadhar Bansal
# Setup:
In your remote PC, do the following:
1.  Clone the repository into the ```catkin_ws/src```. This includes the necessary packages such as ```turtlebot3 navigation```, ```turtlebot3_slam```, ```apriltag_ros```, ```explore_lite```.
2. Go to ```catkin_ws``` and ```catkin_make```.
3. Source the ``catkin_ws``` using ```source devel/setup.bash```

In your Turtlebot3, do the following:
1. ```SSH``` into your raspberrypi of your turtlebot from your remote PC by entering ```sudo ssh ubuntu@ip_address```. Enter the password when required.
2. Install the ```apriltag_ros``` package for apriltag detection using ```sudo apt install ros-noetic-apriltag-ros```
3. Install the ```raspicamnode``` package for raspberrypi camera control using the instructions from ```https://github.com/UbiquityRobotics/raspicam_node.git```
4. Calibrate the camera by following the instructions from the same website.
5. Source the ```catkin_ws``` using ```source devel/setup.bash```

# Execution:
Run ```roscore``` in your PC. Make sure to setup the ~/.bashrc file with the right IP address of the PC and TurtleBot3 and ```ROS_MASTER_URI``` and ```ROS_HOSTNAME``` as per the instructions from ```https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup```
In the Turtlebot3, do the following:
1. To bringup the turtlebot, run ```roslaunch turtlebot3_bringup turtlebot3_robot.launch```
2. To run the raspicam_node, run ```roslaunch raspicam_node camerav2_1280x960_10fps.launch enable_raw:=true```
3. To run the apriltag detection, run ```roslaunch turtlebot3_mr apriltag_gazebo.launch```

In the remote PC, do the following:
1. To execute the move_base node, run ```roslaunch turtlebot3_navigation move_base.launch```
2. To execute the gmapping node, run ```roslaunch turtlebot3_slam turtlebot3_slam.launch```
3. To execute the explore_lite frontier exploration, ```roslaunch explore_lite explore.launch```
4. To record all the topics for future reference, run```rosbag record -a```
5. After exploration, save the map by running ```rosrun map_server map_saver -f ~/map```
6. To view the output of the raspicam_node and /tag_detections node, ```rqt_image_view```
7. Run the pose estimation script by running ```rosrun turtlebot3_navigation detection.py```
