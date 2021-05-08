"""
@file   graphs.py
@author Emil Roy

This file contains the Status Section widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
import pyqtgraph.examples
import pyqtgraph as pg
import constants
import commands
import simulation as sim
import numpy as np

# WIP data plotting widget
containerPressureGraph = pg.GraphicsLayoutWidget()

# get values from example simp values
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

containerPressureGraph.addPlot(y = data, title = "Container Pressure Data")

#graph to check payloads pressure data
payloadPressureGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payloadPressureGraph.addPlot(y = data, title = "Payloads Pressure Data")

#graph to check the containers temperature
containerTempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

containerTempGraph.addPlot(y = data, title = "Container Temperature Data")

#graph to check the payload temperatures
payloadTempGraph = pg.GraphicsLayoutWidget()
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

payloadTempGraph.addPlot(y = data, title = "Payloads Temperature Data")

#TODO might want to have different graphs for each plot
#also confused how voltage plot should be like, should it be
#a plot, or just some text?

def build():
    layout = QGridLayout()
    layout.addWidget(containerPressureGraph, 0, 0)
    layout.addWidget(payloadPressureGraph, 0, 1)
    layout.addWidget(containerTempGraph, 1, 0)
    layout.addWidget(payloadTempGraph, 1, 1)

    return layout

# TODO: add an update function and a loop for plots so they update every second
def update():
    update_graphs()
    pass
