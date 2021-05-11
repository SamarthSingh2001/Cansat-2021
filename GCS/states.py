"""
@file   states.py
@author Emil Roy

This file contains the Status Section widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants
import commands
import simulation

#create payload states/statuses
payloadLabel = QLabel("Payload")#TODO make payload and container label more prominent. Also adjust spacing
payValidPackets = 2
payInvalidPackets = 0
payValidPacketLabel = QLabel("Valid Packets: " + str(payValidPackets))#TODO how do we add packets?
payInvalidPacketLabel = QLabel("Invalid Packets: " + str(payInvalidPackets))

payload1State = QLabel("Payload 1 State: NOT Deployed")
payload1State.setStyleSheet("color: red")

payload2State = QLabel("Payload 2 State: NOT Deployed")
payload2State.setStyleSheet("color: red")

#create container states/statuses
containerLabel = QLabel("Container")
conValidPackets = 6
conInvalidPackets = 2
conValidPacketLabel = QLabel("Valid Packets: " + str(conValidPackets))#TODO how do we add packets?
conInvalidPacketLabel = QLabel("Invalid Packets: " + str(conInvalidPackets))

containerState = QLabel("State: Not Deployed")

# returns a layout that can be included in application window
def build():

    # can add future labels here such as altitude, temperature, etc if wanted

    #adding all the widgets to the layout
    layout = QVBoxLayout()
    layout.addWidget(payloadLabel)
    layout.addWidget(payValidPacketLabel)
    layout.addWidget(payInvalidPacketLabel)
    layout.addWidget(payload1State)
    layout.addWidget(payload2State)

    layout.addWidget(containerLabel)
    layout.addWidget(conValidPacketLabel)
    layout.addWidget(conInvalidPacketLabel)
    layout.addWidget(containerState)

    return layout

#function to update if first payload is deployed or not
def payload1Deployed():
    payload1Label.setText("Payload 1 State: Deployed")
    payload1Label.setStyleSheet("color: green")

#function to update if second payload is deployed or not
def payload2Deployed():
    payload2Label.setText("Payload 2 State: Deployed")
    payload2Label.setStyleSheet("color: green")

#function to update container states
def containerDeployed():
    payload2Label.setText("State: Deployed")
    payload2Label.setStyleSheet("color: green")
