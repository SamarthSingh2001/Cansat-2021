"""
@file   main.py
@author Joshua Tenorio, Emil Roy

Main program for the Ground Station software.
"""
from  PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout
import pyqtgraph.examples
import pyqtgraph as pg
import numpy as np
import cmd_terminal
import status_section
import graphs
import simulation as sim
import constants
import states
import packet_history
import csv_generation
import xbee
import sys
from testing import local_test as test
# uncomment this if running examples
#pyqtgraph.examples.run()


# GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
#window.resize(2000, 1100) 
window.resize(1600, 900)


# widgets
command_terminal: QVBoxLayout = cmd_terminal.build()
status_widget: QVBoxLayout = status_section.build()
graphs_widget: QGridLayout = graphs.build()
pkt_history: QVBoxLayout = packet_history.build()

# stack the packet history on top of command terminal
comm_stack = QVBoxLayout()
comm_stack.addLayout(pkt_history)
comm_stack.addLayout(command_terminal)

# show gui
layout = QHBoxLayout()
layout.addLayout(comm_stack,1)  # graph widget is wider than cmd terminal, which is wider than status widget
layout.addLayout(graphs_widget,4)
layout.addLayout(status_widget,0)

window.setLayout(layout)
#window.setStyleSheet('background-color: #2C2726')
window.show()

# update function
def update():

    # update graph and container/payload states
    graphs.update()

    #status updates
    status_section.mqttStatus(constants.mqtt_flag)
    status_section.simulationStatus(constants.sim_enable_flag, constants.sim_activate_flag)
    status_section.update() # this update function is for mission time
    if constants.sp1_deployed_flag:
        status_section.payload1Deployed()
    if constants.sp2_deployed_flag:
        status_section.payload2Deployed()

    # temporary spot but it probably makes sense here
    if(constants.sim_activate_flag and constants.sim_enable_flag):
        sim_packet = sim.transmit_packet()
        if sim_packet != "null":
            xbee.send_packet(sim_packet)

csv_generation.build()#to create the csv files

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1000)

# local test arg
if len(sys.argv) > 1:
    if sys.argv[1] == "-t":
        test.run()


app.exec()
