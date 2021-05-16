"""
@file mqtt_util.py
@author cansat

Implementation for sending data to MQTT broker for live-remote viewing of data
"""
import paho.mqtt.client as mqtt
import os
import time
# Define event callbacks
csv_data = ""

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
def on_publish(client, obj, mid):
    print("mid: " + str(mid))
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(client, obj, level, string):
    print(string)
# setup mqtt client call backs
mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log

topic = 'teams/3226' # team number
# Connect
mqttc.username_pw_set("t1010", "t1010pass") # made up username and password
for mqtt
#mqttc.connect(url.hostname, url.port) # establish connection
mqttc.connect("cansat.info",1883)

# Publish a message
fd = csv_data # data from the xbee on packet recieved method
dat = fd.read() # read in whole file
fd.close()
dat = dat.split('\n') # split lines
while 1:#REPLACE with update() function in main
    for i in dat: # go through all the lines in the file
        b = i.split(',') # split line to locate element 3
        if len(b) > 1:
            if b[3] == 'C': # check if container data
                time.sleep(1) # insert 1 second interval unless payload adata
            mqttc.publish(topic, i) # send the line of data

def send_packet(string):
    csv_data = string
