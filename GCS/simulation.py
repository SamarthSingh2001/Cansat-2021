"""
@file simulation.py
@author Joshua Tenorio

Functionality and implementation of Simulation Mode
"""


def parse_sim_profile(file_name):
    # figure out file extension bc not sure if it will be in .txt or .csv
    f_extension = file_name.split(".")[1]
    file = open(file_name, mode = "r")
    if f_extension == "txt": # case 1: txt file
        data = []
        for line in file:
            if line[0].strip() != "#" or line.strip() == "":
                print(line[0])
                if line.strip() == "### End of file ###":
                    break
                args = line.split(",")
                data.append(args[0])
        
        print(data[0])
        file.close()
        return data

    elif f_extension == "csv": # case 2: csv file
        pass
    else:
        print("Profile is not a .txt or .csv file")
        return 0
    