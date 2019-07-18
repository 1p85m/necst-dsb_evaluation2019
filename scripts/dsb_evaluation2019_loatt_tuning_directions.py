#!/usr/bin/env python3

name = 'dsb_evaluation2019_loatt_tuning_directions'

import rospy
import time
import std_msgs.msg

import dsb_evaluation2019_controler

rospy.init_node(name)

loatt = dsb_evaluation2019_controller.loatt()

parser = argparse.ArgumentParser(description = 'set Lo Att level')

parser.add_argument('loatt_tuning', type = float, help = 'set Lo Att level')

args = parser.parse_args()

loatt_h.set_vol(loatt_tuning)       #set Lo Att tuning vol
