# control_joystick package

This package contains the Arduino and python scripts for data acquisition of the joystick connected to an Arduino board.

## joystick_test

This script is for test only. It is to test if the Arduino board is successfully connected to the computer and the input data can be plotted.

## joystick_demo

This script is to obtain the joystick input data and publish to a ROS topic.
 
## scripts/joystick_callibration.py

This pythin scripts reads raw joystick input and publishes values between -1 and 1. The output can be callibrated between these values for diffrent joysticks by changing the values of xMin, xMax, xZero, yMin, yMax and yZero in the script. It expects to have the arduino board publish the raw joystick values.



## To publish the raw joystick input from arduino board, run the following command

rosrun rosserial_python serial_node.py /dev/ttyACM0

The port /dev/ttyACM0 needs to be verified