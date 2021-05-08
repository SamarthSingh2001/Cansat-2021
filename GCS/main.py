"""
@file   main.py
@author Joshua Tenorio

Main program for the Ground Station software.
"""
from  PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout
import pyqtgraph.examples
import pyqtgraph as pg
import numpy as np
import cmd_terminal
import status_section
import simulation as sim

# uncomment this if running examples
#pyqtgraph.examples.run()


# GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
window.resize(900, 600)


# widgets
command_terminal: QVBoxLayout = cmd_terminal.build()
status_section: QVBoxLayout = status_section.build()

# WIP data plotting widget
graphs = pg.GraphicsLayoutWidget()

# get values from example simp values
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

graphs.addPlot(y = data, title = "Container Pressure Data")

# TODO: add an update function and a loop for plots so they update every second
def update_graphs():
    pass

# show gui
layout = QHBoxLayout()
layout.addLayout(command_terminal)
layout.addWidget(graphs)
layout.addLayout(status_section)
window.setLayout(layout)
window.show()
# widgets TODO: status indicators for simulation mode, MQTT transmission, payload/container state status perhaps?

# update function
def update():
    update_graphs()
    pass

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1000)

app.exec()
