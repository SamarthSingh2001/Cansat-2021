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
payloadLabel = QLabel("Payload")
payloadLabel.setStyleSheet("color: blue;"
                         "border-style: solid;"
                         "background-color: #87CEFA;"
                         "border-width: 2px;"
                         "border-color: #1E90FF;"
                         "border-radius: 3px")
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
containerLabel.setStyleSheet("color: blue;"
                         "border-style: solid;"
                         "background-color: #87CEFA;"
                         "border-width: 2px;"
                         "border-color: #1E90FF;"
                         "border-radius: 3px")
conValidPackets = 6
conInvalidPackets = 2
conValidPacketLabel = QLabel("Valid Packets: " + str(conValidPackets))#TODO how do we add packets?
conInvalidPacketLabel = QLabel("Invalid Packets: " + str(conInvalidPackets))

containerState = QLabel("State: Not Deployed")
containerState.setStyleSheet("color: red")

# returns layout for payload info
def buildPayLayout():
    #adding all the widgets to the layout
    layout = QVBoxLayout()
    layout.addWidget(payloadLabel)
    layout.addWidget(payValidPacketLabel)
    layout.addWidget(payInvalidPacketLabel)
    layout.addWidget(payload1State)
    layout.addWidget(payload2State)
    return layout

# return container info as layout
def buildContainerLayout():
    layout = QVBoxLayout()
    layout.addWidget(containerLabel)
    layout.addWidget(conValidPacketLabel)
    layout.addWidget(conInvalidPacketLabel)
    layout.addWidget(containerState)
    return layout

#function to update if first payload is deployed or not
def payload1Deployed():
    payload1State.setText("Payload 1 State: Deployed")
    payload1State.setStyleSheet("color: green")

#function to update if second payload is deployed or not
def payload2Deployed():
    payload2State.setText("Payload 2 State: Deployed")
    payload2State.setStyleSheet("color: green")

#function to update container states
def containerDeployed():
    containerState.setText("State: Deployed")
    containerState.setStyleSheet("color: green")
