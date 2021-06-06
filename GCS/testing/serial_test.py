import serial

ser = serial.Serial('/dev/ttyUSB0')
print(ser.name)
ser.write(b'hello')
ser.close()