"""
@file   csv_generation.py
@author Emil Roy

This file contains the CSV Generation file.
"""
import csv
from csv import writer

#create the 3 csv files required
def build():
    #write to container csv file
    with open('reports/Flight_3226_C.csv', 'w', newline='') as f:
        writerC = csv.writer(f)
        #create the csv headers
        writerC.writerow(['TEAM_ID','MISSION_TIME','PACKET_COUNT','PACKET_TYPE','MODE',
                        'SP1_RELEASED','SP2_RELEASED','ALTITUDE','TEMP',
                        'VOLTAGE','GPS_TIME','GPS_LATITUDE','GPS_LONGITUDE',
                        'GPS_ALTITUDE','GPS_SATS','SOFTWARE_STATE',
                        'SP1_PACKET_COUNT','SP2_PACKET_COUNT','CMD_ECHO'])

    #write to payload 1 csv file
    with open('reports/Flight_3226_SP1.csv', 'w', newline='') as f:
        writerSP1 = csv.writer(f)
        #create the csv headers
        writerSP1.writerow(['TEAM_ID','MISSION_TIME','PACKET_COUNT','PACKET_TYPE',
                            'SP_ALTITUDE','SP_TEMP','SP_ROTATION_RATE'])

    #write to payload 2 csv file
    with open('reports/Flight_3226_SP2.csv', 'w', newline='') as f:
        writerSP2 = csv.writer(f)
        #create the csv headers
        writerSP2.writerow(['TEAM_ID','MISSION_TIME','PACKET_COUNT','PACKET_TYPE',
                            'SP_ALTITUDE','SP_TEMP','SP_ROTATION_RATE'])

#to append data to the csv files
def append_csv_file(line):
    data = line.split(",")
    type = data[3] #to check if it came from container or which payload
    #appends data to the proper csv file
    if type == 'C':
        with open('reports/Flight_3226_C.csv', 'a') as ad:
            writer_object = writer(ad)
            writer_object.writerow(data)
            ad.close()
    if type == 'S1':
        with open('reports/Flight_3226_SP1.csv', 'a') as ad:
            writer_object = writer(ad)
            writer_object.writerow(data)
            ad.close()
    if type == 'S2':
        with open('reports/Flight_3226_SP2.csv', 'a') as ad:
            writer_object = writer(ad)
            writer_object.writerow(data)
            ad.close()
    else: #should there be some errors?
        pass
