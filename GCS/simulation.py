"""
@file simulation.py
@author Joshua Tenorio

Functionality and implementation of Simulation Mode
"""

# TODO: add a way to specify the filename for simulation file
import csv

def parse_sim_profile(file_name):
    # figure out file extension bc not sure if it will be in .txt or .csv
    f_extension = file_name.split(".")[1]
    file = open(file_name, mode = "r")
    if f_extension == "txt": # case 1: txt file
        data = []
        for line in file:
            if line[0].strip() != "#" or line.strip() == "":
                if line.strip() == "### End of file ###":
                    break
                args = line.split(",")
                if len(args) > 1:
                    data.append(args[3])

        file.close()
        return data

    elif f_extension == "csv": # case 2: csv file
        with open(file, 'r') as file:
            reader = csv.reader(file)

            data=[]
            for row in reader:#TODO how to test this?
                data.append(row[3])

            file.close()
            return data
    else:
        print("Profile is not a .txt or .csv file")
        return 0


err_out_of_bounds = "SIM ERR: attempted to retrieve a packet out of profile's bounds"
# returns the nth val in the sim profile to transmit to container
def get_nth_value(n):
    sim_profile = parse_sim_profile("simp_cmd_example.txt") # TODO: this can be optimized by caching this result in a file global variable
    if n < 0 or n >= len(sim_profile):
        print(err_out_of_bounds)
        return err_out_of_bounds

    # if n is a valid packet num, return the packet
    return sim_profile[n]


def transmit_packet():
    data = get_nth_value(transmit_packet.itr)
    if (data != err_out_of_bounds):
        packet = "CMD,3226,SIMP," + str(data)
        print(packet)
        transmit_packet.itr += 1
        return packet
    else:
        transmit_packet.itr += 1
        return "null"

transmit_packet.itr = 0
