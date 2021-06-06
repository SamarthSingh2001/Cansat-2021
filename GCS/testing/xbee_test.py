from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/ttyUSB0", 9600)
device.open()

def callback(message):
    data = message.data.decode("utf8")
    print("packet:" + data)

device.add_data_received_callback(callback)