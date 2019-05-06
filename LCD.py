from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
from Functions import Power_LCD, Battery_Charge

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd


lcd_columns = 16
lcd_rows = 2
 
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)
 
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)


def LCD():
    
    power = Power_LCD()
    BatCharge = Battery_Charge()
    
    lcd_line_1 = 'Power:' + power +'mW\n' 
 
    
    lcd_line_2 = 'BatCha:' + BatCharge +'%'
 
    
    lcd.message = lcd_line_1 + lcd_line_2
 
    sleep(10)
    lcd.clear()


while True:
    LCD()
    
