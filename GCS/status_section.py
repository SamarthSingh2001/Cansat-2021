"""
@file   status_section.py
@author Emil Roy

This file contains the Status Section widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants
import commands
import simulation

# returns a layout that can be included in application window
def build():

    #create widget to show simulation status
    simulationOn = False
    simulationLabel = QLabel("Simulation Mode Status: False")
    simulationLabel.setStyleSheet("color: red")

    #create widget to show MQTT Transmission status
    mqttOn = False
    mqttTransmitLabel = QLabel("MQTT Transmission Status: False")
    mqttTransmitLabel.setStyleSheet("color: red")

    #create widget to show if first payload is deployed
    payload1Label = QLabel("Payload 1 Is NOT Deployed")
    payload1Label.setStyleSheet("color: red")

    #create widget to show if second payload is deployed
    payload2Label = QLabel("Payload 2 Is NOT Deployed")
    payload2Label.setStyleSheet("color: red")

    # can add future labels here such as altitude, temperature, etc if wanted

    #adding all the widgets to the layout
    layout = QVBoxLayout()
    layout.addWidget(simulationLabel)
    layout.addWidget(mqttTransmitLabel)
    layout.addWidget(payload1Label)
    layout.addWidget(payload2Label)

    return layout

#function to update simulation status
def simulationStatus(status):
    if (status == False):
        simulationLabel = QLabel("Simulation Mode Status: False")
        simulationLabel.setStyleSheet("color: red")
    else:
        simulationLabel = QLabel("Simulation Mode Status: True")
        simulationLabel.setStyleSheet("color: green")
    pass

#function to update MQTT transmission status
def mqttStatus(status):
    if (status == False):
        mqttTransmitLabel = QLabel("MQTT Transmission Status: False")
        mqttTransmitLabel.setStyleSheet("color: red")
    else:
        mqttTransmitLabel = QLabel("MQTT Transmission Status: True")
        mqttTransmitLabel.setStyleSheet("color: green")
    pass

#function to update if first payload is deployed or not
def payload1Deployed():
    payload1Label.setText("Payload 1 Is SUCCESSFULLY Deployed")
    payload1Label.setStyleSheet("color: green")
    pass

#function to update if second payload is deployed or not
def payload2Deployed():
    payload2Label.setText("Payload 2 Is SUCCESSFULLY Deployed")
    payload2Label.setStyleSheet("color: green")
    pass
