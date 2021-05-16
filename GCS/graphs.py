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
containerPressureGraph = pg.GraphicsLayoutWidget()

# get values from example simp values
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

containerPressureGraph.addPlot(y = data, title = "Container Pressure Data")


#graph to check the containers temperature
containerTempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

containerTempGraph.addPlot(y = data, title = "Container Temperature Data")

#graph to check the containers altitude
containerAltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

containerAltitudeGraph.addPlot(y = data, title = "Container Altitude Data")


#PAYLOAD 1 STUFF BELOW------------------------------------------------------------

#graph to check payloads pressure data
payload1PressureGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload1PressureGraph.addPlot(y = data, title = "Payload 1 Pressure Data")
#graph to check the payload temperatures
payload1TempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload1TempGraph.addPlot(y = data, title = "Payload 1 Temperature Data")

#graph to check the payload altitude
payload1AltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload1AltitudeGraph.addPlot(y = data, title = "Payload 1 Altitude Data")

#graph to check the payload speed
payload1SpeedGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload1SpeedGraph.addPlot(y = data, title = "Payload 1 Speed Data")

#PAYLOAD 2 Stuff Below-----------------------------------------------------
payload2PressureGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload2PressureGraph.addPlot(y = data, title = "Payload 2 Pressure Data")
#graph to check the payload temperatures
payload2TempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload2TempGraph.addPlot(y = data, title = "Payload 2 Temperature Data")

#graph to check the payload altitude
payload2AltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload2AltitudeGraph.addPlot(y = data, title = "Payload 2 Altitude Data")

#graph to check the payload speed
payload2SpeedGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payload2SpeedGraph.addPlot(y = data, title = "Payload 2 Speed Data")


#TODO might want to have different graphs for each plot
#also confused how voltage plot should be like, should it be
#a plot, or just some text?

def build():
    layout = QGridLayout()
    payWidget: QVBoxLayout = states.buildPayLayout()
    conWidget: QVBoxLayout = states.buildContainerLayout()
    layout.addLayout(payWidget, 0, 0)
    layout.addWidget(payload1TempGraph, 0, 1)
    layout.addWidget(payload1PressureGraph, 0, 2)
    layout.addWidget(payload1AltitudeGraph, 0, 3)
    layout.addWidget(payload1SpeedGraph, 0, 4)
    #Adding payload 2 graphs now
    layout.addWidget(payload2TempGraph, 1, 1)
    layout.addWidget(payload2PressureGraph, 1, 2)
    layout.addWidget(payload2AltitudeGraph, 1, 3)
    layout.addWidget(payload2SpeedGraph, 1, 4)


    layout.setRowMinimumHeight(2, 50)#adds spacing between payloads and container
    #TODO add way to seperate payload and container stuff better
    layout.addLayout(conWidget, 4, 0)
    layout.addWidget(containerTempGraph, 4, 1)
    layout.addWidget(containerPressureGraph, 4, 2)
    layout.addWidget(containerAltitudeGraph, 5, 1)


    return layout


# TODO: implement update function
def update():
    pass

def update_data(packet):
    pass