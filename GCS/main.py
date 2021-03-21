"""
@file   main.py
@author Joshua Tenorio

Main program for the Ground Station software. 
"""
from  PyQt5.QtWidgets import QApplication, QWidget
import cmd_terminal

# TODO: make a custom class that inherits line edit perhaps? so that we can properly declare event handlers/signals
# update: nvm current solution is kinda nice

# GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. Ground Station")

# widgets
command_terminal = cmd_terminal.build()


window.setLayout(command_terminal)
window.show()


app.exec_()


