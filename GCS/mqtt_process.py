"""
@file mqtt_util.py
@author cansat/Emil

Implementation for processing data to MQTT broker for live-remote viewing of data
"""
import mqtt.*
MQTTClient client
def setup() :
    client = new MQTTClient(this);
    client.connect("mqtt://3226:Kaukteti492%@cansat.info");


void draw()

def keyPressed():
    client.publish("teams/3226", "world");

def clientConnected() :
    println("client connected");
# client.subscribe("/hello");

def messageReceived(String topic, byte[] payload) :
    println("new message: " + topic + " - " + new String(payload));

def connectionLost() :
    println("connection lost");
