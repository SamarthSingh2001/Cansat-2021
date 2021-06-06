from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress

device = XBeeDevice("/dev/ttyUSB0", 9600)
device.open()

def callback(message):
    data = message.data.decode("utf8")
    print("packet:" + data)
    if data == "":
        print("newline recieved")

device.add_data_received_callback(callback)
remote = RemoteXBeeDevice(device,
            XBee64BitAddress.from_hex_string("13A200415CCC25"))
device.send_data(remote, "CMD,SIMP,3226,15151515\n")
while True:
    pass