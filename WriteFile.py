from Functions import Voltage, Current, Power,Radiation, A_Radiation, Alitidue
import datetime 
from time import sleep
from pysolar.solar import radiation

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M_{fname}'):
      return datetime.datetime.now().strftime(fmt).format(fname=fname)



while True:
      outf = open(timeStamped('Voltage.txt'),'a+')
      
      outf.write("Voltage , %f" % Voltage())

      outf.write(", Current , %f" % Current())

      outf.write(", Power , %f" % Power())

      outf.write(", Clear Sky Irradiance, %f" % Radiation(radiation))

      outf.write(", Actual Irradiance , %f\r\n" % A_Radiation())

      outf.close()

      sleep(2)







