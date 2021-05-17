"""
@file   local_test.py
@author Joshua Tenorio

Contains the Local Test GUI for testing GCS in real time.
"""
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget
from testing import sensors


window = QWidget()
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. GCS Local Test Suite")
window.resize(450,100)
layout = QVBoxLayout()
setDataButton = QPushButton("Randomize Data")
sendCPacketButton = QPushButton("Send Container Packet")
sendSp1PacketButton = QPushButton("Send SP1 Packet")
sendSp2PacketButton = QPushButton("Send SP2 Packet")

layout.addWidget(setDataButton)
layout.addWidget(sendCPacketButton)
layout.addWidget(sendSp1PacketButton)
layout.addWidget(sendSp2PacketButton)
window.setLayout(layout)

setDataButton.clicked.connect(sensors.randomizeData)
sendCPacketButton.clicked.connect(sensors.sendContainerPacket)
sendSp1PacketButton.clicked.connect(sensors.sendPayloadPacket1)
sendSp2PacketButton.clicked.connect(sensors.sendPayloadPacket2)


def run():
    window.show()