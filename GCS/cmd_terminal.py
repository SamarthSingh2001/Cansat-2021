from  PyQt5.QtWidgets import QApplication, QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import constants
import commands

def constructor():
    # prefix for commands to be sent to container
    cmd_prefix = "CMD," + str(constants.team_number)

    command_label = QLabel("Command Terminal")
    command_history = QPlainTextEdit()
    command_history.setFocusPolicy(Qt.NoFocus)
    command_input = QLineEdit()

    command_layout = QVBoxLayout()
    command_layout.addWidget(command_label)
    command_layout.addWidget(command_history)
    command_layout.addWidget(command_input)

    # temporary event handlers
    def send_command():
        command = command_input.text()

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
            command_history.appendPlainText(cmd_packet)
            command_input.clear()


    command_input.returnPressed.connect(send_command)

    return command_layout


