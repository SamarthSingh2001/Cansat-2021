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


#PAYLOAD STUFF BELOW------------------------------------------------------------

#graph to check payloads pressure data
payloadPressureGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payloadPressureGraph.addPlot(y = data, title = "Payloads Pressure Data")
#graph to check the payload temperatures
payloadTempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payloadTempGraph.addPlot(y = data, title = "Payloads Temperature Data")

#graph to check the payload altitude
payloadAltitudeGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payloadAltitudeGraph.addPlot(y = data, title = "Payloads Altitude Data")

#graph to check the payload speed
payloadSpeedGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payloadSpeedGraph.addPlot(y = data, title = "Payloads Speed Data")



#TODO might want to have different graphs for each plot
#also confused how voltage plot should be like, should it be
#a plot, or just some text?

def build():
    layout = QGridLayout()
    payWidget: QVBoxLayout = states.buildPayLayout()
    conWidget: QVBoxLayout = states.buildContainerLayout()
    layout.addLayout(payWidget, 0, 0)
    layout.addWidget(payloadTempGraph, 0, 1)
    layout.addWidget(payloadPressureGraph, 0, 2)
    layout.addWidget(payloadAltitudeGraph, 1, 1)
    layout.addWidget(payloadSpeedGraph, 1, 2)

    #TODO add way to seperate payload and container stuff better
    layout.addLayout(conWidget, 4, 0)
    layout.addWidget(containerTempGraph, 4, 1)
    layout.addWidget(containerPressureGraph, 4, 2)
    layout.addWidget(containerAltitudeGraph, 5, 1)


    return layout


# TODO: implement update function
def update():
    pass
