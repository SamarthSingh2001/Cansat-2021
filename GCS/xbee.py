"""
@file xbee.py
@author Joshua Tenorio

Implementation for transmitting and receiving packets to and from the Container
"""
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import csv_generation as csv_gen
import mqtt_util as mqtt
import graphs
import status_section as status
import packet_history




device = XBeeDevice("/dev/ttyUSB0", 9600)

# this address could change
container64Addr = "13A200418C7122"


remote = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string(container64Addr))

# initialize the Xbee radio
def initialize():
    device.open()
    device.add_data_received_callback(on_packet_received)
    return True

# send a packet to the container Xbee
def send_packet(packet):
    device.send_data(remote, packet)
    return True

# callback function when a packet from the Container is received
def on_packet_received(xbee_message):
    data = xbee_message.data.decode("utf8")
    csv_gen.append_csv_file(data)
    mqtt.send_packet(data)
    graphs.update_data(data)
    status.updateMissionTime(data)
    packet_history.packet_received(data)
    print(data)


# to be used for local test suite
def local_packet_test(data):
    csv_gen.append_csv_file(data)
    mqtt.send_packet(data)
    graphs.update_data(data)
    status.updateMissionTime(data)
    packet_history.packet_received(data)