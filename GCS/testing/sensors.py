"""
@file   sensors.py
@author Joshua Tenorio

Generate random data to send to GCS
"""
import random
from xbee import local_packet_test

# common packet info
TEAM_ID = 3226
time_h = 0
time_m = 0
time_s = 0
MISSION_TIME = str(time_h) + ":" + str(time_m) + ":" + str(time_s)
PACKET_COUNT = 0

# container packet info
MODE = "F"                          # const for now
SP1_RELEASED = "N"
SP2_RELEASED = "N"
ALTITUDE = 0.0
TEMP = 30.0
VOLTAGE = 9.00
GPS_TIME = MISSION_TIME # o3o
GPS_LATITUDE = 0.0000
GPS_LONGITUDE = 0.0000
GPS_ALTITUDE = 0.1
GPS_SATS = 0
SOFTWARE_STATE = "LAUNCH_WAIT"
SP1_PACKET_COUNT = 0
SP2_PACKET_COUNT = 0
CMD_ECHO = "CXON"                    # const for now

# SP1 packet info
SP_ALTITUDE_1 = 700.0
SP_TEMP_1 = 25.0
SP_ROTATION_RATE_1 = 0

# SP2 packet info
SP_ALTITUDE_2 = 700.0
SP_TEMP_2 = 25.0
SP_ROTATION_RATE_2 = 0

def randomizeData():
    global time_h, time_m, time_s, PACKET_COUNT, MISSION_TIME
    global MODE, SP1_RELEASED, SP2_RELEASED, ALTITUDE, TEMP, VOLTAGE, GPS_TIME, GPS_LATITUDE, GPS_LONGITUDE, GPS_ALTITUDE, GPS_SATS, SOFTWARE_STATE, SP1_PACKET_COUNT, SP2_PACKET_COUNT
    global SP_ALTITUDE_1, SP_TEMP_1, SP_ROTATION_RATE_1
    global SP_ALTITUDE_2, SP_TEMP_2, SP_ROTATION_RATE_2

    # set the new mission time in a sane manner
    time_s += 1
    if time_s == 60:
        time_s = 0
        time_m += 1
    if time_m == 60:
        time_m = 0
        time_h += 1
    if time_h == 24:
        time_h = 0
    MISSION_TIME = str(time_h) + ":" + str(time_m) + ":" + str(time_s)

    # randomize data
    SP1_RELEASED = random.choice(["N", "R"])
    SP2_RELEASED = random.choice(["N", "R"])
    ALTITUDE += random.randint(-5, 5)
    TEMP += random.randint(-3, 3)
    VOLTAGE += random.randint(-1, 1)
    GPS_TIME = MISSION_TIME
    GPS_LATITUDE += random.randint(-100, 100) # l u d i c r o u s  s p e e d
    GPS_LONGITUDE += random.randint(-100, 100)
    GPS_ALTITUDE += random.randint(-5, 5)
    GPS_SATS += random.randint(-20, 20)
    SOFTWARE_STATE = random.choice(["LAUNCH_WAIT", "ASCENT", "DESCENT", "LANDED"]) # incomplete list but these are the only ones we track

    SP_ALTITUDE_1 += random.randint(-10, 2)
    SP_ALTITUDE_2 += random.randint(-10, 2)

    SP_TEMP_1 += random.randint(-3, 3)
    SP_TEMP_2 += random.randint(-3, 3)

    SP_ROTATION_RATE_1 += random.randint(-600, 600)
    SP_ROTATION_RATE_2 += random.randint(-600, 600)


def sendContainerPacket():
    global PACKET_COUNT
    PACKET_COUNT += 1
    telemetry = (
        str(TEAM_ID) + "," + MISSION_TIME + "," + str(PACKET_COUNT) + "," + "C" + "," + MODE + "," + SP1_RELEASED + "," + SP2_RELEASED + "," + str(ALTITUDE) + "," + str(TEMP) + "," + str(VOLTAGE) + "," +
        GPS_TIME + "," + str(GPS_LATITUDE) + "," + str(GPS_LONGITUDE) + "," + str(GPS_ALTITUDE) + "," + str(GPS_SATS) + "," + SOFTWARE_STATE + "," + str(SP1_PACKET_COUNT) + "," + str(SP2_PACKET_COUNT) + "," +
        CMD_ECHO
    )
    local_packet_test(telemetry)

def returnPayloadPacket(num):
    global PACKET_COUNT, SP1_PACKET_COUNT, SP2_PACKET_COUNT
    PACKET_COUNT += 1
    if num == 1:
        SP1_PACKET_COUNT += 1
        telemetry = (
            str(TEAM_ID) + "," + MISSION_TIME + "," + str(PACKET_COUNT) + "," + "S1" + "," + str(SP_ALTITUDE_1) + "," + str(SP_TEMP_1) + "," + str(SP_ROTATION_RATE_1)
        )
        return telemetry
    else:
        SP2_PACKET_COUNT += 1
        telemetry = (
            str(TEAM_ID) + "," + MISSION_TIME + "," + str(PACKET_COUNT) + "," + "S2" + "," + str(SP_ALTITUDE_2) + "," + str(SP_TEMP_2) + "," + str(SP_ROTATION_RATE_2)
        )
        return telemetry

def sendPayloadPacket1():
    local_packet_test(returnPayloadPacket(1))

def sendPayloadPacket2():
    local_packet_test(returnPayloadPacket(2))