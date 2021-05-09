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
    
def sim_command(args):
    if args[1] == "ENABLE":
        constants.sim_enable_flag = True
        return True, ""
    elif args[1] == "ACTIVATE":
        constants.sim_activate_flag = True
        return True, ""
    elif args[1] == "DISABLE":
        constants.sim_activate_flag = False
        constants.sim_enable_flag = False
        return True, ""
    else:
        print("CMD ERR: SIM expected {ENABLE,ACTIVATE,DISABLE} but found " + args[1])
        return False, ("CMD ERR: SIM expected {ENABLE,ACTIVATE,DISABLE} but found " + args[1])

def transmission_toggle(args):
    if args[0] == "CX":
        if args[1] == "ON":
            constants.cx_flag = True
            return True, ""
        elif args[1] == "OFF":
            constants.cx_flag = False
            return True, ""
        else:
            print("CMD ERR: CX expected {ON,OFF} but found " + args[1])
            return False, ("CMD ERR: CX expected {ON,OFF} but found " + args[1])
    elif args[0] == "SP1X":
        if args[1] == "ON":
            constants.sp1x_flag = True
            return True, ""
        elif args[1] == "OFF":
            constants.sp1x_flag = False
            return True, ""
        else:
            print("CMD ERR: SP1X expected {ON,OFF} but found " + args[1])
            return False, ("CMD ERR: SP1X expected {ON,OFF} but found " + args[1])
    else:
        if args[1] == "ON":
            constants.sp2x_flag = True
            return True, ""
        elif args[1] == "OFF":
            constants.sp2x_flag = False
            return True, ""
        else:
            print("CMD ERR: SP2X expected {ON,OFF} but found " + args[1])
            return False, ("CMD ERR: SP2X expected {ON,OFF} but found " + args[1])

def mqtt_toggle(args):
    if args[1] == "ON":
        constants.mqtt_flag = True
        return True, ""
    elif args[1] == "OFF":
        constants.mqtt_flag = False
        return True, ""
    else:
        print("CMD ERR: MQTT expected {ON,OFF} but found " + args[1])
        return False, ("CMD ERR: MQTT expected {ON,OFF} but found " + args[1])