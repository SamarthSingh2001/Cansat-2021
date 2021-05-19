"""
@file   graphs.py
@author Emil Roy, Joshua Tenorio

This file contains the Graphs and States widgets.
"""
from  PyQt5.QtWidgets import QLabel, QPlainTextEdit, QLineEdit, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import states
import simulation as sim
import numpy as np

# used for stand in values
initial_array = [0] * 120 # create a List of 120 zero's
initial_cx = np.empty(120)
initial_sp1x = np.array(list(range(-120, 0)))
initial_sp2x = np.array(list(range(-120, 0)))

# graph the containers voltage
containerVoltageGraph = pg.GraphicsLayoutWidget()
containerVoltageData = np.array(initial_array).astype(float)
cvPlot = containerVoltageGraph.addPlot(title = "Container Voltage Data")
containerVoltageCurve = cvPlot.plot(containerVoltageData)
cvPlot.setLabel('left', "Volts(V)")
cvPlot.setLabel('bottom', "# of Packets")

#graph to check the containers temperature
containerTempGraph = pg.GraphicsLayoutWidget()
containerTempData = np.array(initial_array).astype(float)
ctPlot = containerTempGraph.addPlot(title = "Container Temperature Data")
containerTempCurve = ctPlot.plot(containerTempData)
ctPlot.setLabel('left', "Temperature(C°)")
ctPlot.setLabel('bottom', "# of Packets")

#graph to check the containers altitude
containerAltitudeGraph = pg.GraphicsLayoutWidget()
containerAltitudeData = np.array(initial_array).astype(float)
caPlot = containerAltitudeGraph.addPlot(title = "Container Altitude Data")
containerAltitudeCurve = caPlot.plot(containerAltitudeData)
caPlot.setLabel('left', "Altitude(m)")
caPlot.setLabel('bottom', "# of Packets")

#PAYLOAD 1 STUFF BELOW------------------------------------------------------------

#graph to check the payload temperatures
payload1TempGraph = pg.GraphicsLayoutWidget()
p1TempData = np.array(initial_array).astype(float)
p1tPlot = payload1TempGraph.addPlot(title = "Payload 1 Temperature Data")
p1TempCurve = p1tPlot.plot(p1TempData)
p1tPlot.setLabel('left', "Temperature(C°)")
p1tPlot.setLabel('bottom', "# of Packets")

#graph to check the payload altitude
payload1AltitudeGraph = pg.GraphicsLayoutWidget()
p1AltitudeData = np.array(initial_array).astype(float)
p1aPlot = payload1AltitudeGraph.addPlot(title = "Payload 1 Altitude Data")
p1AltitudeCurve = p1aPlot.plot(p1AltitudeData)
p1aPlot.setLabel('left', "Altitude(m)")
p1aPlot.setLabel('bottom', "# of Packets")

#graph to check the payload speed
payload1RotationRateGraph = pg.GraphicsLayoutWidget()
p1RPMdata = np.array(initial_array).astype(float)
p1rPlot = payload1RotationRateGraph.addPlot(title = "Payload 1 Rotation Rate Data")
p1RPMcurve = p1rPlot.plot(p1RPMdata)
p1rPlot.setLabel('left', "Rotations Per Minute(RPM)")
p1rPlot.setLabel('bottom', "# of Packets")

#PAYLOAD 2 Stuff Below-----------------------------------------------------

#graph to check the payload temperatures
payload2TempGraph = pg.GraphicsLayoutWidget()
p2TempData = np.array(initial_array).astype(float)
p2tPlot = payload2TempGraph.addPlot(title = "Payload 2 Temperature Data")
p2TempCurve = p2tPlot.plot(p2TempData)
p2tPlot.setLabel('left', "Temperature(C°)")
p2tPlot.setLabel('bottom', "# of Packets")

#graph to check the payload altitude
payload2AltitudeGraph = pg.GraphicsLayoutWidget()
p2AltitudeData = np.array(initial_array).astype(float)
p2aPlot = payload2AltitudeGraph.addPlot(title = "Payload 2 Altitude Data")
p2AltitudeCurve = p2aPlot.plot(p2AltitudeData)
p2aPlot.setLabel('left', "Altitude(m)")
p2aPlot.setLabel('bottom', "# of Packets")

#graph to check the payload speed
payload2RotationRateGraph = pg.GraphicsLayoutWidget()
p2RPMdata = np.array(initial_array).astype(float)
p2rPLot = payload2RotationRateGraph.addPlot(title = "Payload 2 Rotation Rate Data")
p2RPMcurve = p2rPLot.plot(p2RPMdata)
p2rPLot.setLabel('left', "Rotations Per Minute(RPM)")
p2rPLot.setLabel('bottom', "# of Packets")


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
    #add container stuff
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
    if containerPtr > 119:
        containerVoltageCurve.setData(containerVoltageData)
        containerAltitudeCurve.setData(containerAltitudeData)
        containerTempCurve.setData(containerTempData)
        containerVoltageCurve.setPos(containerPtr-120, containerPtr)
        containerAltitudeCurve.setPos(containerPtr-120, containerPtr)
        containerTempCurve.setPos(containerPtr-120, containerPtr)
    else:
        containerVoltageCurve.setData(containerVoltageData[:containerPtr])
        containerAltitudeCurve.setData(containerAltitudeData[:containerPtr])
        containerTempCurve.setData(containerTempData[:containerPtr])


    #update payloads
    if p1Ptr > 119:
        p1RPMcurve.setData(p1RPMdata)
        p1AltitudeCurve.setData(p1AltitudeData)
        p1TempCurve.setData(p1TempData)
        p1RPMcurve.setPos(p1Ptr-120, p1Ptr)
        p1AltitudeCurve.setPos(p1Ptr-120, p1Ptr)
        p1TempCurve.setPos(p1Ptr-120, p1Ptr)
    else:
        p1RPMcurve.setData(p1RPMdata[:p1Ptr])
        p1AltitudeCurve.setData(p1AltitudeData[:p1Ptr])
        p1TempCurve.setData(p1TempData[:p1Ptr])

    if p2Ptr > 119:
        p2RPMcurve.setData(p2RPMdata)
        p2AltitudeCurve.setData(p2AltitudeData)
        p2TempCurve.setData(p2TempData)
        p2RPMcurve.setPos(p2Ptr-120, p2Ptr)
        p2AltitudeCurve.setPos(p2Ptr-120, p2Ptr)
        p2TempCurve.setPos(p2Ptr-120, p2Ptr)
    else:
        p2RPMcurve.setData(p2RPMdata[:p2Ptr])
        p2AltitudeCurve.setData(p2AltitudeData[:p2Ptr])
        p2TempCurve.setData(p2TempData[:p2Ptr])


# given a packet, update arrays
def update_data(packet):
    global containerAltitudeData, containerVoltageData, containerTempData
    global p1AltitudeData, p1RPMdata, p1TempData
    global p2AltitudeData, p2RPMdata, p2TempData
    global containerPtr, p1Ptr, p2Ptr

    # send packet to states widget
    states.update_state(packet)

    # parse packet for stuff to update
    packet_args = packet.split(",")

    if packet_args[3] == "C":
        if containerPtr > 119:
            containerPtr += 1
            containerAltitudeData[:-1] = containerAltitudeData[1:]
            containerAltitudeData[-1] = float(packet_args[7])

            containerTempData[:-1] = containerTempData[1:]
            containerTempData[-1] = float(packet_args[8])

            containerVoltageData[:-1] = containerVoltageData[1:]
            containerVoltageData[-1] = float(packet_args[9])
        else:
            containerAltitudeData[containerPtr] = float(packet_args[7])
            containerTempData[containerPtr] = float(packet_args[8])
            containerVoltageData[containerPtr] = float(packet_args[9])
            containerPtr += 1

    elif packet_args[3] == "S1":
        if p1Ptr > 119:
            p1Ptr += 1
            p1AltitudeData[:-1] = p1AltitudeData[1:]
            p1AltitudeData[-1] = float(packet_args[4])

            p1TempData[:-1] = p1TempData[1:]
            p1TempData[-1] = float(packet_args[5])

            p1RPMdata[:-1] = p1RPMdata[1:]
            p1RPMdata[-1] = float(packet_args[6])
        else:
            p1AltitudeData[p1Ptr] = float(packet_args[4])
            p1TempData[p1Ptr] = float(packet_args[5])
            p1RPMdata[p1Ptr] = float(packet_args[6])
            p1Ptr += 1

    elif packet_args[3] == "S2":
        if p2Ptr > 119:
            p2Ptr += 1
            p2AltitudeData[:-1] = p2AltitudeData[1:]
            p2AltitudeData[-1] = float(packet_args[4])

            p2TempData[:-1] = p2TempData[1:]
            p2TempData[-1] = float(packet_args[5])

            p2RPMdata[:-1] = p2RPMdata[1:]
            p2RPMdata[-1] = float(packet_args[6])
        else:
            p2AltitudeData[p1Ptr] = float(packet_args[4])
            p2TempData[p1Ptr] = float(packet_args[5])
            p2RPMdata[p1Ptr] = float(packet_args[6])
            p2Ptr += 1
    else:
        print("GRAPH ERR: invalid packet")
