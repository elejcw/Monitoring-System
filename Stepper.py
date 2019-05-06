import RPi.GPIO as GPIO
from time import sleep
import sys
from Functions import Azimuth, A_Radiation
                                        #assign GPIO pins for motor
motor_channel = (29,31,33,35)  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                                            #for defining more than 1 GPIO channel as input/output use
GPIO.setup(motor_channel, GPIO.OUT)


Azimuth = Azimuth()
Actual_Irradiance =  A_Radiation()
outf=open('Position.txt','r')
Position = outf.read()
Position = int(Position)
outf.close()


def Write():
    outW = open('Position.txt','w')
    outW.write(str(i))
    outW.close()


##looped

Position = Position - int((Azimuth - 90) * 1.4)

if Position < 0 and 90<Azimuth<270:
    Position = abs(Position)
    for i in range (Position):
    
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.02)
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.02)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(0.02)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(0.02)
        i = i
        Write()
        
        
        
        
elif Position >0 and 90<Azimuth<270: 
    for i in range (Position):
        
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.02)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(0.02)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(0.02)
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.02)
        i = i
        Write()


