"""
@file   cmd_terminal.py
@author Joshua Tenorio

This file contains the Command Terminal widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import constants
import commands
import simulation

# needs to be file-global so it can be edited
error_label = QLabel("")
error_label.setStyleSheet("color: red")

valid_cmd_flag = True

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
    layout.addWidget(error_label)

    # event handler
    def send_command():
        command = input.text()

        # only do stuff if there is things in command input
        if command != "":

            cmd_packet = cmd_prefix
            cmd_args = command.upper().split()
            for arg in cmd_args:
                cmd_packet = cmd_packet + "," + arg
            
            valid_cmd_flag = True
            error_msg = ""
            if cmd_args[0] == "ST":
                times = commands.set_utc_time()
                cmd_packet += "," + str(times[0]) + ":" + str(times[1]) + ":" + str(times[2])
            elif cmd_args[0] == "SIM": # TODO: maybe add another elif but for sim and release? so this is only sim and enable/activate/disable
                valid_cmd_flag, error_msg = commands.sim_command(cmd_args)
            elif cmd_args[0] == "CX" or cmd_args[0] == "SP1X" or cmd_args[0] == "SP2X":
                valid_cmd_flag, error_msg = commands.transmission_toggle(cmd_args)
            elif cmd_args[0] == "MQTT":
               valid_cmd_flag, error_msg =  commands.mqtt_toggle(cmd_args)
            else:
                error_msg = "CMD ERR: Command not recognized"
                print(error_msg)
                
                valid_cmd_flag = False

            # append command to history
            # TODO: add some sort of indicator that a command failed, maybe red font?
            history.appendPlainText(cmd_packet)
            input.clear()

            # TODO: send cmd_packet to container xbee radio
            if valid_cmd_flag:
                error_label.setText("")
                # send command if valid
            else:
                error_label.setText(error_msg)

    input.returnPressed.connect(send_command)

    # temp code for testing simulation
    # TODO: transfer this into commands.py
    simulation.parse_sim_profile("simp_cmd_example.txt")

    return layout


