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
    csv_gen.append_csv_file(xbee_message)
    mqtt.send_packet(xbee_message)
    graphs.update_data(xbee_message)
    status.updateMissionTime(xbee_message)
    packet_history.packet_received(xbee_message)

    # TODO: parse xbee_message into a List
    #       send relevant items to relevant widgets
