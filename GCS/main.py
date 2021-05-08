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
graphs: QGridLayout = graphs.build()

# show gui
layout = QHBoxLayout()
layout.addLayout(command_terminal)
layout.addLayout(graphs)
layout.addLayout(status_section)
window.setLayout(layout)
window.show()
# widgets TODO: status indicators for simulation mode, MQTT transmission, payload/container state status perhaps?

timer = pg.QtCore.QTimer()
timer.timeout.connect(graphs.update)
timer.start(1000)

app.exec()
