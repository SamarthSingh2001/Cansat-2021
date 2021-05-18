"""
@file mqtt_util.py
@author cansat/Emil

Implementation for sending data to MQTT broker for live-remote viewing of data
"""
import paho.mqtt.client as mqtt
import os
import time
# Define event callbacks

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
mqttc.username_pw_set("3226", "Kaukteti492%") # made up username and password

#mqttc.connect(url.hostname, url.port) # establish connection
mqttc.connect("cansat.info",1883)

def send_packet(message):
    mqttc.publish("teams/3226", message)
