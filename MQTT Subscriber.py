import paho.mqtt.client as mqtt
import time
import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H_{fname}'):
  return datetime.datetime.now().strftime(fmt).format(fname=fname)

def on_message(mosq, obj, msg):
  print(msg.payload)
  fd = open(timeStamped('Voltage.csv'), 'wb')
  fd.write(msg.payload)

client = mqtt.Client("P2")                               
client.connect("broker.mqttdashboard.com", 1883, 60)                
client.subscribe("SolarPanel/Voltage",0)
client.on_message = on_message                           

while True:                                             
   client.loop()
