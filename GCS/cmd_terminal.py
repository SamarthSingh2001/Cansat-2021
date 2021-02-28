"""
@file   cmd_terminal.py
@author Joshua Tenorio

This file contains the Command Terminal widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants
import commands

# returns a layout that can be included in application window
def build():
    # prefix for commands to be sent to container
    cmd_prefix = "CMD," + str(constants.team_number)

    label = QLabel("Command Terminal")
    history = QPlainTextEdit()
    history.setFocusPolicy(Qt.NoFocus)
    input = QLineEdit()

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(history)
    layout.addWidget(input)

    # temporary event handlers
    def send_command():
        command = input.text()

        # only do stuff if there is things in command input
        if command != "":

            cmd_packet = cmd_prefix
            cmd_args = command.upper().split()
            for arg in cmd_args:
                cmd_packet = cmd_packet + "," + arg
            # TODO: write code for sending cmd packet to container, need to test xbee first probably
            # TODO: put in a if/else block here for acting on the command if necessary

            if cmd_args[0] == "ST":
                times = commands.set_utc_time()
                cmd_packet += "," + str(times[0]) + ":" + str(times[1]) + ":" + str(times[2])

            # append command to 
            history.appendPlainText(cmd_packet)
            input.clear()

    input.returnPressed.connect(send_command)
    return layout


