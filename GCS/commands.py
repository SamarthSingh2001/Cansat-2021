"""
@file   commands.py
@author Joshua Tenorio

Command functionality is defined here.
"""
from datetime import datetime
import constants

def parse_input(command):
    pass

def set_utc_time():
    now = datetime.now()
    
    # convert from MST to UTC
    utc_hour = (now.hour + 7) % 24
    utc_minute = now.minute
    utc_second = now.second
    return [utc_hour, utc_minute, utc_second]
    
def sim_toggle(args):
    if args[1] == "enable":
        constants.sim_enable_flag = True
        return True
    elif args[1] == "activate":
        constants.sim_activate_flag = True
        return True
    elif args[1] == "disable":
        constants.sim_activate_flag = False
        constants.sim_enable_flag = False
        return True
    else:
        print("CMD ERR: sim expected {enable,activate,disable} but found " + args[1])
        return False 
