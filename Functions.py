import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import datetime
import pytz
import math
import io

from ina219 import INA219, DeviceRangeError
from pysolar.solar import radiation
from pysolar.solar import get_altitude
from pysolar.solar import get_azimuth
import pysolar

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS =2.0
ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, address = 0x40)
ina.configure(ina.RANGE_16V)
i=1
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

latitude_deg = 52.7721
longitude_deg = 1.2062

def Azimuth():
        now = datetime.datetime.now()
        date = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,tzinfo=pytz.utc)
        
        Azimuth = get_azimuth(latitude_deg,longitude_deg, date)
        
        return Azimuth

def Alitidue():
    altitude_deg = int(get_altitude(latitude_deg, longitude_deg, date))
    
    return altitude_deg


def Radiation(radiation):
        now = datetime.datetime.now()
        date = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,tzinfo=pytz.utc)

        Azimuth = get_azimuth(latitude_deg,longitude_deg, date)


        altitude_deg = int(get_altitude(latitude_deg, longitude_deg, date))


        radiation = float(radiation.get_radiation_direct(date, altitude_deg))
       
        return radiation

def Voltage():
    Voltage = ina.voltage()
    Voltage = round(Voltage,2)
    return Voltage

def Current():
    Current = (ina.current()/1000)
    Current = round(Current,2)
    return Current

def Power():
    Power = ina.power()
    Power = round(Power,2)
    return Power

def Power_LCD():
        Power = ina.power()
        Power = round(Power,2)
        Power = repr(Power)
        return Power

def A_Radiation():
    V = Voltage()
    Rs = 0.017
    I = Current()
    q = 1.6e-19
    K = 1.38e-23
    A = 1.2
    T = 293
    N = 28
    vt = q/(A*K*T*N)
    Is = I/(math.exp(V+((I+Rs)/vt)) - 1)
    Isc = 250e-3

    G = (((I-Is)*((math.exp((V+(I+Rs))/vt))-1))/Isc)*1000
    G = round(G,2)
    return G

def Temperature():
    f = open("/sys/class/thermal/thermal_zone0/temp","r")
    t = float(f.readline())
    cputemp = t/1000
    return cputemp

def Battery_Charge():
    value =float(mcp.read_adc_difference(1))
    BatVolt= ((value/1023)*3.3)
    BatVolt = (BatVolt/0.1666666667)
    
    if BatVolt >13.5:       
        BatCha= 100
        
    elif 13<BatVolt<13.5:
        BatCha = 80
        
    elif 12.5<BatVolt<13:
         BatCha = 60
        
    elif 12<BatVolt<12.5:
         BatCha = 40
        
    elif 11.5<BatVolt<12:
         BatCha = 20
         
    elif BatVolt < 11.5:
        BatCha = 0 

    BatCha = repr(BatCha)
    return BatCha
    
