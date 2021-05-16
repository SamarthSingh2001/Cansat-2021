"""
@file   graphs.py
@author Emil Roy

This file contains the Status Section widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph.examples
import pyqtgraph as pg
import constants
import commands
import states
import simulation as sim
import numpy as np

# data plotting widget
containerVoltageGraph = pg.GraphicsLayoutWidget()

# get values from example simp values
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
containerVoltageData = np.array(simp_values).astype(float)

containerVoltageGraph.addPlot(y = containerVoltageData, title = "Container Voltage Data")


#graph to check the containers temperature
containerTempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
containerTempData = np.array(simp_values).astype(float)

containerTempGraph.addPlot(y = containerTempData, title = "Container Temperature Data")

#graph to check the containers altitude
containerAltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
containerAltitudeData = np.array(simp_values).astype(float)

containerAltitudeGraph.addPlot(y = containerAltitudeData, title = "Container Altitude Data")


#PAYLOAD 1 STUFF BELOW------------------------------------------------------------

#graph to check the payload temperatures
payload1TempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
p1TempData = np.array(simp_values).astype(float)

payload1TempGraph.addPlot(y = p1TempData, title = "Payload 1 Temperature Data")

#graph to check the payload altitude
payload1AltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
p1AltitudeData = np.array(simp_values).astype(float)

payload1AltitudeGraph.addPlot(y = p1AltitudeData, title = "Payload 1 Altitude Data")

#graph to check the payload speed
payload1RotationRateGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
p1RPMdata = np.array(simp_values).astype(float)

payload1RotationRateGraph.addPlot(y = p1RPMdata, title = "Payload 1 Rotation Rate Data")

#PAYLOAD 2 Stuff Below-----------------------------------------------------

#graph to check the payload temperatures
payload2TempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
p2TempData = np.array(simp_values).astype(float)

payload2TempGraph.addPlot(y = p2TempData, title = "Payload 2 Temperature Data")

#graph to check the payload altitude
payload2AltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
p2AltitudeData = np.array(simp_values).astype(float)

payload2AltitudeGraph.addPlot(y = p2AltitudeData, title = "Payload 2 Altitude Data")

#graph to check the payload speed
payload2RotationRateGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
p2RPMdata = np.array(simp_values).astype(float)

payload2RotationRateGraph.addPlot(y = p2RPMdata, title = "Payload 2 Rotation Rate Data")


#TODO might want to have different graphs for each plot
#also confused how voltage plot should be like, should it be
#a plot, or just some text?

def build():
    layout = QGridLayout()
    payWidget: QVBoxLayout = states.buildPayLayout()
    conWidget: QVBoxLayout = states.buildContainerLayout()
    layout.addLayout(payWidget, 0, 0)
    layout.addWidget(payload1TempGraph, 0, 1)
    layout.addWidget(payload1AltitudeGraph, 0, 2)
    layout.addWidget(payload1RotationRateGraph, 0, 3)
    #Adding payload 2 graphs now
    layout.addWidget(payload2TempGraph, 1, 1)
    layout.addWidget(payload2AltitudeGraph, 1, 2)
    layout.addWidget(payload2RotationRateGraph, 1, 3)


    layout.setRowMinimumHeight(2, 50)#adds spacing between payloads and container
    #TODO add way to seperate payload and container stuff better
    layout.addLayout(conWidget, 4, 0)
    layout.addWidget(containerTempGraph, 4, 1)
    layout.addWidget(containerVoltageGraph, 4, 2)
    layout.addWidget(containerAltitudeGraph, 5, 1)


    return layout

# these variables are used for updating the graphs
containerPtr = 0
p1Ptr = 0
p2Ptr = 0

# TODO: implement update function
# ie setData setPos functions
def update():
    pass

# given a packet, update arrays
def update_data(packet):
    global containerAltitudeData, containerVoltageData, containerTempData
    global p1AltitudeData, p1RPMdata, p1TempData
    global p2AltitudeData, p2RPMdata, p2TempData
    global containerPtr, p1Ptr, p2Ptr

    # parse packet for stuff to update
    packet_args = packet.split(",")
    if packet_args[3] == "C":
        # TODO: update container/payload state widgets
        containerPtr += 1
        containerAltitudeData[:-1] = containerAltitudeData[1:]
        containerAltitudeData[-1] = packet_args[7]

        containerTempData[:-1] = containerTempData[1:]
        containerTempData[-1] = packet_args[8]

        containerVoltageData[:-1] = containerVoltageData[1:]
        containerVoltageData[-1] = packet_args[9]
    elif packet_args[3] == "S1":
        p1Ptr += 1
        p1AltitudeData[:-1] = p1AltitudeData[1:]
        p1AltitudeData[-1] = packet_args[4]

        p1TempData[:-1] = p1TempData[1:]
        p1TempData[-1] = packet_args[5]

        p1RPMdata[:-1] = p1RPMdata[1:]
        p1RPMdata[-1] = packet_args[6]
    elif packet_args[3] == "S2":
        p2Ptr += 1
        p2AltitudeData[:-1] = p2AltitudeData[1:]
        p2AltitudeData[-1] = packet_args[4]

        p2TempData[:-1] = p2TempData[1:]
        p2TempData[-1] = packet_args[5]

        p2RPMdata[:-1] = p2RPMdata[1:]
        p2RPMdata[-1] = packet_args[6]
    else:
        print("GRAPH ERR: invalid packet")
