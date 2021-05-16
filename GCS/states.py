"""
@file   states.py
@author Emil Roy

This file contains the States Section widget. It contains various statuses relating to the container and the payloads.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants
import commands


#create payload states/statuses
payload1Label = QLabel("Payload 1")
payload1Label.setStyleSheet("color: blue;"
                         "border-style: solid;"
                         "background-color: #87CEFA;"
                         "border-width: 2px;"
                         "border-color: #1E90FF;"
                         "border-radius: 3px")
pay1ValidPackets = 2 #example values
pay1InvalidPackets = 0
pay1ValidPacketLabel = QLabel("Valid Packets: " + str(pay1ValidPackets))#TODO how do we add packets?
pay1InvalidPacketLabel = QLabel("Invalid Packets: " + str(pay1InvalidPackets))


payload2Label = QLabel("Payload 2")
payload2Label.setStyleSheet("color: blue;"
                         "border-style: solid;"
                         "background-color: #87CEFA;"
                         "border-width: 2px;"
                         "border-color: #1E90FF;"
                         "border-radius: 3px")
pay2ValidPackets = 2 #example values
pay2InvalidPackets = 0
pay2ValidPacketLabel = QLabel("Valid Packets: " + str(pay2ValidPackets))#TODO how do we add packets?
pay2InvalidPacketLabel = QLabel("Invalid Packets: " + str(pay2InvalidPackets))

payload1State = QLabel("Payload 1 State: Launchpad and Not Deployed")
payload1State.setStyleSheet("color: red")

payload2State = QLabel("Payload 2 State: Launchpad and Not Deployed")
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

conVoltage = 4 #placeholder
conVoltageLabel = QLabel("Voltage: " + str(conVoltage))

containerState = QLabel("State: Launchpad")
containerState.setStyleSheet("color: red")

# returns layout for payload info
def buildPayLayout():
    #adding all the widgets to the layout
    layout = QVBoxLayout()
    # payload 1
    layout.addWidget(payload1Label)
    layout.addWidget(pay1ValidPacketLabel)
    layout.addWidget(pay1InvalidPacketLabel)
    layout.addWidget(payload1State)


    # payload 2
    layout.addWidget(payload2Label)
    layout.addWidget(pay2ValidPacketLabel)
    layout.addWidget(pay2InvalidPacketLabel)
    layout.addWidget(payload2State)
    return layout

# return container info as layout
def buildContainerLayout():
    layout = QVBoxLayout()
    layout.addWidget(containerLabel)
    layout.addWidget(conValidPacketLabel)
    layout.addWidget(conInvalidPacketLabel)
    layout.addWidget(containerState)
    layout.addWidget(conVoltageLabel)
    return layout

#function to update first payload states
def updatePayload1State(state):
    if(state == "deployed"):
        payload1State.setText("Payload 1 State: Deployed and Descending")
        payload1State.setStyleSheet("color: green")

#function to update if second payload states
def updatePayload2State(state):
    if (state == "deployed"):
        payload2State.setText("Payload 2 State: Deployed and Descending")
        payload2State.setStyleSheet("color: green")

#function to update container states
def updateContainerState(state):
    if(state == "asending"):
        containerState.setText("State: Ascending")
        containerState.setStyleSheet("color: green")
        payload1State.setText("Payload 1 State: Ascending and NOT Deployed")
        payload1State.setStyleSheet("color: yellow")
        payload2State.setText("Payload 2 State: Ascending and NOT Deployed")
        payload2State.setStyleSheet("color: yellow")

    elif(state == "descending"):
        containerState.setText("State: Descending")
        containerState.setStyleSheet("color: yellow")
    elif(state == "landed"):
        containerState.setText("State: Landed")
        containerState.setStyleSheet("color: purple")
    #TODO what if input wrong cmd?
