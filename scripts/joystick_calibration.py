import rospy
from geometry_msgs.msg import Vector3, Point, Twist

pub = rospy.Publisher('/py/joystick', Point, queue_size=5)

class CalibrateJoystick():
    def __init__(self, joystick_topic = '/py/joystick', raw_joystick_topic = '/arduino/joystick_raw'):
        self.joystick_topic = joystick_topic
        self.raw_joystick_topic = raw_joystick_topic
        self.joystick_publisher_point = rospy.Publisher(joystick_topic+"_point", Point, queue_size=10)
        self.joystick_publisher_twist = rospy.Publisher(joystick_topic+"_twist", Twist, queue_size=10)
        rospy.Subscriber(raw_joystick_topic, Vector3, self.raw_joystick_cb)
        self.xMax = 952
        self.xMin = 8
        self.xZero = 478

        self.yMax = 963
        self.yMin = 10
        self.yZero = 495

        self.vMax = [self.xMax, self.yMax]
        self.vMin = [self.xMin, self.yMin]
        self.vZero = [self.xZero, self.yZero]


    

    def raw_joystick_cb(self, raw_joystick_msg):
        
        joy_msg = Point()
        joy_msg_twist = Twist()
        
        rawValue = [raw_joystick_msg.x, raw_joystick_msg.y]
        cValue = [0,0]

        for i in range(0,2):
            if(rawValue[i] > self.vMax[i]) :
                cValue[i]= 1
    
            else :
                if (rawValue[i] > self.vZero[i]):
                    cValue[i] = (rawValue[i] - self.vZero[i]) / (self.vMax[i]-self.vZero[i])
                else:
                    if(rawValue[i] > self.vMin[i]):
                        cValue[i] = (rawValue[i] - self.vZero[i]) / (self.vZero[i] - self.vMin[i])
                    else:
                        cValue[i] = -1
                
        joy_msg.x = cValue[1]
        joy_msg.y = -1*cValue[0]

        joy_msg_twist.linear.x = joy_msg.x
        joy_msg_twist.angular.z = joy_msg.y
    



        self.joystick_publisher_point.publish(joy_msg)
        self.joystick_publisher_twist.publish(joy_msg_twist)


if __name__ == '__main__':
    #local_planner_topic = "/local_planner/cmd_vel"
    #cmd_vel_topic = "/digital_twin/cmd_vel"
    rospy.init_node('CallibrateJoystick', anonymous=True)
    a = CalibrateJoystick()
    rospy.spin()
