from  PyQt5.QtWidgets import QApplication, QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import constants

# prefix for commands to be sent to container
command_prefix = "CMD," + str(constants.team_number)

# GUI
app = QApplication([])
#label = QLabel("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
#label.show()
command_history = QPlainTextEdit()
command_history.setFocusPolicy(Qt.NoFocus)
command_input = QLineEdit()

command_layout = QVBoxLayout()
command_layout.addWidget(command_history)
command_layout.addWidget(command_input)

window = QWidget()
window.setLayout(command_layout)
window.show()

# temporary event handlers
def send_command():
    command = command_input.text()
    command_history.appendPlainText(command)
    command_input.clear()

    # the command to be sent to container, WIP
    print(command_prefix)


command_input.returnPressed.connect(send_command)

app.exec_()

# TODO: make a custom class that inherits line edit so that we can properly declare event handlers/signals
# TODO: separate command related stuff to its own file

