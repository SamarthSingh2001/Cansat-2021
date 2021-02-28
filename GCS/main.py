from  PyQt5.QtWidgets import QApplication, QLabel, QPlainTextEdit, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import cmd_terminal



# GUI
app = QApplication([])
#label = QLabel("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
#label.show()
command_terminal = cmd_terminal.constructor()
window = QWidget()
window.setLayout(command_terminal)
window.setWindowTitle("Team 3226 P.O.P.T.A.R.T.S. Ground Station")
window.show()


app.exec_()

# TODO: make a custom class that inherits line edit perhaps? so that we can properly declare event handlers/signals
# update: nvm current solution is kinda nice

