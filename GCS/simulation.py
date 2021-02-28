"""
@file simulation.py
@author Joshua Tenorio

Functionality and implementation of Simulation Mode
"""


def parse_sim_profile(file_name):
    # figure out file extension bc not sure if it will be in .txt or .csv
    f_extension = file_name.split(".")[1]
    #file = open(file_name, mode = "r")
    
    if f_extension == "txt": # case 1: txt file
        pass
    elif f_extension == "csv": # case 2: csv file
        pass
    else:
        print("Profile not a .txt or .csv file")
        return 0
    