import paho.mqtt.client as mqtt
import time
import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M_{fname}'):
    return (datetime.datetime.now()).strftime(fmt).format(fname=fname)


broker_address="broker.mqttdashboard.com"
client = mqtt.Client("P1")                                
client.connect("test.mosquitto.org.", 1883, 60)

while True:
    outf = open(timeStamped('Voltage.txt'),'r')
    data = outf.read()                                          
    client.publish(topic="SolarPanel/Voltage", payload=data ,qos=0)
    time.sleep(10)
    


