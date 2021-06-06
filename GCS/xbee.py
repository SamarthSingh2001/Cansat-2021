"""
@file xbee.py
@author Joshua Tenorio

Implementation for transmitting and receiving packets to and from the Container
"""
from digi.xbee.devices import XBeeDevice
import csv_generation as csv_gen
import mqtt_util as mqtt
import graphs
import status_section as status
import packet_history

import serial

#ser = serial.Serial('dev/ttyUSB0')
#print(ser.name)
#ser.write(b'hello')
#ser.close()

# placeholder xbee object
# note: VERY subject to change
device = XBeeDevice("COM1", 9600)

# initialize the Xbee radio
def initialize():
    device.open()
    device.add_data_received_callback(on_packet_received)
    return True

# send a packet to the container Xbee
def send_packet(packet):
    return True

# callback function when a packet from the Container is received
def on_packet_received(xbee_message):
    data = xbee_message.data.decode("utf8")
    csv_gen.append_csv_file(data)
    mqtt.send_packet(data)
    graphs.update_data(data)
    status.updateMissionTime(data)
    packet_history.packet_received(data)

    # TODO: parse xbee_message into a List
    #       send relevant items to relevant widgets
