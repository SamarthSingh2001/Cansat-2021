"""
@file   commands.py
@author Joshua Tenorio

Command functionality is defined here.
"""
from datetime import datetime


def set_utc_time():
    now = datetime.now()
    
    # convert from MST to UTC
    utc_hour = (now.hour + 7) % 24
    utc_minute = now.minute
    utc_second = now.second
    return [utc_hour, utc_minute, utc_second]
    