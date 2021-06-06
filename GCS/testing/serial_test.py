import serial

ser = serial.Serial('/dev/ttyUSB0', timeout=5)
print(ser.name)
#ser.write(b'hello\n')
print("waiting for line...")

packet: bytes = ser.read_until(size=32)
#packet: bytes = ser.readline()

print("packet: " + packet.decode("utf-8"))
ser.close()