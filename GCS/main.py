"""
@file   main.py
@author Joshua Tenorio

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

# uncomment this if running examples
#pyqtgraph.examples.run()


# GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
window.resize(2000, 1100)


# widgets
command_terminal: QVBoxLayout = cmd_terminal.build()
status_widget: QVBoxLayout = status_section.build()
graphs_widget: QGridLayout = graphs.build()

# show gui
layout = QHBoxLayout()
layout.addLayout(command_terminal,1)  # graph widget is wider than cmd terminal, which is wider than status widget
layout.addLayout(graphs_widget,4)
layout.addLayout(status_widget,0)
window.setLayout(layout)
window.show()

# update function
def update():
    graphs.update()

    #status updates
    status_section.mqttStatus(constants.mqtt_flag)
    status_section.simulationStatus(constants.sim_enable_flag, constants.sim_activate_flag)
    if constants.sp1_deployed_flag:
        status_section.payload1Deployed()
    if constants.sp2_deployed_flag:
        status_section.payload2Deployed()


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1000)

# TODO: do we need another timer for sending simulation stuff to container? only needed if our GUI update is < 1000 ms

app.exec()
