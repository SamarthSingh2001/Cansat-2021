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
pay1ValidPackets = 0
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
pay2ValidPackets = 0
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
conValidPackets = 0
conInvalidPackets = 0
conValidPacketLabel = QLabel("Valid Packets: " + str(conValidPackets))#TODO how do we add packets?
conInvalidPacketLabel = QLabel("Invalid Packets: " + str(conInvalidPackets))

containerState = QLabel("State: Launchpad")
containerState.setStyleSheet("color: red")

# Container GPS info
gpsTime = "no info received"
gpsLat = 0.0
gpsLon = 0.0
gpsAlt = 0.0
gpsSats = 0

gpsTimeLabel = QLabel("GPS Time (UTC): " + gpsTime)
gpsCoordLabel = QLabel("GPS Coords: " + str(gpsLat) + ", " + str(gpsLon))
gpsAltLabel = QLabel("GPS Altitude (m): " + str(gpsAlt))
gpsSatsLabel = QLabel(str(gpsSats) + " GPS satellites tracking Container")

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
    layout.addWidget(gpsTimeLabel)
    layout.addWidget(gpsCoordLabel)
    layout.addWidget(gpsAltLabel)
    layout.addWidget(gpsSatsLabel)
    return layout

#function to update first payload states
def updatePayload1State(state):
    if(state == "R"):
        payload1State.setText("Payload 1 State: Deployed and Descending")
        payload1State.setStyleSheet("color: green")

#function to update if second payload states
def updatePayload2State(state):
    if (state == "R"):
        payload2State.setText("Payload 2 State: Deployed and Descending")
        payload2State.setStyleSheet("color: green")

#function to update container states
def updateContainerState(state):
    if(state == "ASCENT"):
        containerState.setText("State: Ascending")
        containerState.setStyleSheet("color: green")
        payload1State.setText("Payload 1 State: Ascending and NOT Deployed")
        payload1State.setStyleSheet("color: yellow")
        payload2State.setText("Payload 2 State: Ascending and NOT Deployed")
        payload2State.setStyleSheet("color: yellow")

    elif(state == "DESCENT"):
        containerState.setText("State: Descending")
        containerState.setStyleSheet("color: yellow")
    elif(state == "LANDED"):
        containerState.setText("State: Landed")
        containerState.setStyleSheet("color: purple")

def update_packet_count(packetCount, sp1PacketCount, sp2PacketCount):
    # update variables
    global pay1ValidPackets, pay2ValidPackets, conValidPackets
    if packetCount + sp1PacketCount + sp2PacketCount == -3:
        pay1ValidPackets += 1
    elif packetCount + sp1PacketCount + sp2PacketCount == -6:
        pay2ValidPackets += 1
    else:
        pay1ValidPackets = sp1PacketCount
        pay2ValidPackets = sp2PacketCount
        conValidPackets = packetCount - sp1PacketCount - sp2PacketCount

    # update labels
    pay1ValidPacketLabel.setText("Valid Packets: " + str(pay1ValidPackets))
    pay2ValidPacketLabel.setText("Valid Packets: " + str(pay2ValidPackets))
    conValidPacketLabel.setText("Valid Packets: " + str(conValidPackets))

def update_gps(time, lat, lon, alt, sats):
    global gpsTime, gpsLat, gpsLon, gpsAlt, gpsSats
    gpsTime = time
    gpsLat = lat
    gpsLon = lon
    gpsAlt = alt
    gpsSats = sats

    gpsTimeLabel.setText("GPS Time (UTC): " + gpsTime)
    gpsCoordLabel.setText("GPS Coords: " + str(gpsLat) + ", " + str(gpsLon))
    gpsAltLabel.setText("GPS Altitude (m): " + str(gpsAlt))
    gpsSatsLabel.setText(str(gpsSats) + " GPS satellites tracking Container")


def update_state(packet):
    packet_args = packet.split(",")
    if packet_args[3] == "C":
        # update states
        updatePayload1State(packet_args[5])
        updatePayload2State(packet_args[6])
        updateContainerState(packet_args[15])
        
        # update gps information
        update_gps(packet_args[10], packet_args[11], packet_args[12], packet_args[13], packet_args[14])

        # next, update packet counts regardless of type of packet
        update_packet_count(int(packet_args[2]), int(packet_args[16]), int(packet_args[17]))
    elif packet_args[3] == "S1":
        update_packet_count(-1, -1, -1)
    elif packet_args[3] == "S2":
        update_packet_count(-2, -2, -2)