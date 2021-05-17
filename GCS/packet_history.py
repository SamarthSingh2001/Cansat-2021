"""
@file   packet_history.py
@author Joshua Tenorio

This file contains the Packet History widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants

label = QLabel("Packet History")
history = QPlainTextEdit()
history.setFocusPolicy(Qt.NoFocus)

def build():
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(history)

    return layout

# to be used in the xbee.data_received_callback(message) function
# each packet will be appended to the QPlainTextEdit history widget
def packet_received(packet):
    history.appendPlainText(packet + "\n")