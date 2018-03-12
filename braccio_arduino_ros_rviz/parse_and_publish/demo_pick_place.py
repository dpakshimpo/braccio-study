import rospy
import std_msgs as msg

class Pick_and_Place(object):

    def __init__(self):
        """ Constructor """
        rospy.init_node('pick_place_node', anonymous=False)
        self.joint_arr_pub = rospy.Publisher("joint_array", msg, queue_size=20)
        self.joint_state_sub = rospy.Subscriber("joint_states",msg,joint_state_cb)
    
    def joint_state_cb(self):
        "Call back for joint_state data published from Rviz"
        
        self.joint_arr_pub.publish(data)


