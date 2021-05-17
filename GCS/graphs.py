"""
@file   graphs.py
@author Emil Roy

This file contains the Status Section widget.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import states
import simulation as sim
import numpy as np

# used for stand in values
simp_values = sim.parse_sim_profile("simp_cmd_example.txt")
initial_array = [0] * 120 # create a List of 120 zero's

# graph the containers voltage
containerVoltageGraph = pg.GraphicsLayoutWidget()
containerVoltageData = np.array(simp_values).astype(float)
cvPlot = containerVoltageGraph.addPlot(title = "Container Voltage Data")
containerVoltageCurve = cvPlot.plot(containerVoltageData)

#graph to check the containers temperature
containerTempGraph = pg.GraphicsLayoutWidget()
containerTempData = np.array(simp_values).astype(float)
ctPlot = containerTempGraph.addPlot(title = "Container Temperature Data")
containerTempCurve = ctPlot.plot(containerTempData)

#graph to check the containers altitude
containerAltitudeGraph = pg.GraphicsLayoutWidget()
containerAltitudeData = np.array(simp_values).astype(float)
caPlot = containerAltitudeGraph.addPlot(title = "Container Altitude Data")
containerAltitudeCurve = caPlot.plot(containerAltitudeData)

#PAYLOAD 1 STUFF BELOW------------------------------------------------------------

#graph to check the payload temperatures
payload1TempGraph = pg.GraphicsLayoutWidget()
p1TempData = np.array(simp_values).astype(float)
p1tPlot = payload1TempGraph.addPlot(title = "Payload 1 Temperature Data")
p1TempCurve = p1tPlot.plot(p1TempData)

#graph to check the payload altitude
payload1AltitudeGraph = pg.GraphicsLayoutWidget()
p1AltitudeData = np.array(simp_values).astype(float)
p1aPlot = payload1AltitudeGraph.addPlot(title = "Payload 1 Altitude Data")
p1AltitudeCurve = p1aPlot.plot(p1AltitudeData)

#graph to check the payload speed
payload1RotationRateGraph = pg.GraphicsLayoutWidget()
p1RPMdata = np.array(simp_values).astype(float)
p1rPlot = payload1RotationRateGraph.addPlot(title = "Payload 1 Rotation Rate Data")
p1RPMcurve = p1rPlot.plot(p1RPMdata)

#PAYLOAD 2 Stuff Below-----------------------------------------------------

#graph to check the payload temperatures
payload2TempGraph = pg.GraphicsLayoutWidget()
p2TempData = np.array(simp_values).astype(float)
p2tPlot = payload2TempGraph.addPlot(title = "Payload 2 Temperature Data")
p2TempCurve = p2tPlot.plot(p2TempData)

#graph to check the payload altitude
payload2AltitudeGraph = pg.GraphicsLayoutWidget()
p2AltitudeData = np.array(simp_values).astype(float)
p2aPlot = payload2AltitudeGraph.addPlot(title = "Payload 2 Altitude Data")
p2AltitudeCurve = p2aPlot.plot(p2AltitudeData)

#graph to check the payload speed
payload2RotationRateGraph = pg.GraphicsLayoutWidget()
p2RPMdata = np.array(simp_values).astype(float)
p2rPLot = payload2RotationRateGraph.addPlot(title = "Payload 2 Rotation Rate Data")
p2RPMcurve = p2rPLot.plot(p2RPMdata)



def build():
    layout = QGridLayout()
    payWidget: QVBoxLayout = states.buildPayLayout()
    conWidget: QVBoxLayout = states.buildContainerLayout()
    layout.addLayout(payWidget, 0, 0)
    layout.addWidget(payload1TempGraph, 0, 1)
    layout.addWidget(payload1AltitudeGraph, 0, 2)
    layout.addWidget(payload1RotationRateGraph, 0, 3)
    #Adding payload 2 graphs now
    layout.addWidget(payload2TempGraph, 1, 1)
    layout.addWidget(payload2AltitudeGraph, 1, 2)
    layout.addWidget(payload2RotationRateGraph, 1, 3)


    layout.setRowMinimumHeight(2, 10)#adds spacing between payloads and container
    #TODO add way to seperate payload and container stuff better
    layout.addLayout(conWidget, 3, 0)
    layout.addWidget(containerTempGraph, 3, 1)
    layout.addWidget(containerAltitudeGraph, 3, 2)
    layout.addWidget(containerVoltageGraph, 3, 3)
    
    return layout

# these variables are used for updating the graphs
containerPtr = 0
p1Ptr = 0
p2Ptr = 0

# TODO: implement update function
# ie setData setPos functions
def update():
    # update container
    containerVoltageCurve.setData(containerVoltageData)
    containerVoltageCurve.setPos(containerPtr, 0)
    containerAltitudeCurve.setData(containerAltitudeData)
    containerAltitudeCurve.setPos(containerPtr, 0)
    containerTempCurve.setData(containerTempData)
    containerTempCurve.setPos(containerPtr, 0)

    #update payloads
    p1RPMcurve.setData(p1RPMdata)
    p1RPMcurve.setPos(p1Ptr, 0)
    p1AltitudeCurve.setData(p1AltitudeData)
    p1AltitudeCurve.setPos(p1Ptr, 0)
    p1TempCurve.setData(p1TempData)
    p1TempCurve.setPos(p1Ptr, 0)

    p2RPMcurve.setData(p2RPMdata)
    p2RPMcurve.setPos(p2Ptr, 0)
    p2AltitudeCurve.setData(p2AltitudeData)
    p2AltitudeCurve.setPos(p2Ptr, 0)
    p2TempCurve.setData(p2TempData)
    p2TempCurve.setPos(p2Ptr, 0)


# given a packet, update arrays
def update_data(packet):
    global containerAltitudeData, containerVoltageData, containerTempData
    global p1AltitudeData, p1RPMdata, p1TempData
    global p2AltitudeData, p2RPMdata, p2TempData
    global containerPtr, p1Ptr, p2Ptr

    # parse packet for stuff to update
    packet_args = packet.split(",")
    if packet_args[3] == "C":
        # TODO: update container/payload state widgets
        containerPtr += 1
        containerAltitudeData[:-1] = containerAltitudeData[1:]
        containerAltitudeData[-1] = float(packet_args[7])

        containerTempData[:-1] = containerTempData[1:]
        containerTempData[-1] = float(packet_args[8])

        containerVoltageData[:-1] = containerVoltageData[1:]
        containerVoltageData[-1] = float(packet_args[9])
    elif packet_args[3] == "S1":
        p1Ptr += 1
        p1AltitudeData[:-1] = p1AltitudeData[1:]
        p1AltitudeData[-1] = float(packet_args[4])

        p1TempData[:-1] = p1TempData[1:]
        p1TempData[-1] = float(packet_args[5])

        p1RPMdata[:-1] = p1RPMdata[1:]
        p1RPMdata[-1] = float(packet_args[6])
    elif packet_args[3] == "S2":
        p2Ptr += 1
        p2AltitudeData[:-1] = p2AltitudeData[1:]
        p2AltitudeData[-1] = float(packet_args[4])

        p2TempData[:-1] = p2TempData[1:]
        p2TempData[-1] = float(packet_args[5])

        p2RPMdata[:-1] = p2RPMdata[1:]
        p2RPMdata[-1] = float(packet_args[6])
    else:
        print("GRAPH ERR: invalid packet")

