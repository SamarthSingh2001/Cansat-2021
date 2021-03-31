"""
@file   main.py
@author Joshua Tenorio

Main program for the Ground Station software. 
"""
from  PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
import pyqtgraph.examples
import pyqtgraph as pg
import numpy as np
import cmd_terminal
import simulation as sim


pyqtgraph.examples.run()
# TODO: make a custom class that inherits line edit perhaps? so that we can properly declare event handlers/signals
# update: nvm current solution is kinda nice

# GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
window.resize(400, 300)

# widgets
command_terminal = cmd_terminal.build()
# WIP data plotting widget

win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('Telemetry')

simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
data = np.array(simp_values).astype(float)

win.addPlot(y=data, title="Container Pressure Data")
"""
p1 = win.addPlot()
#data1 = np.array(simp_values)
data1 = np.random.normal(size=300)
curve1 = p1.plot(data1)
ptr1 = 0
def update1():
    global data1, ptr1
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    data1[-1] = np.random.normal()
    curve1.setData(data1)
    
    ptr1 += 1

timer = pg.QtCore.QTimer()
timer.timeout.connect(update1)
timer.start(50)
"""
#layout = QHBoxLayout()
#layout.addChildLayout(command_terminal)
#graph_container = QHBoxLayout()
#layout.addWidget(pw)

window.setLayout(command_terminal)
window.show()


app.exec_()


