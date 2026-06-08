#About: Displays Text to an LCD
#Created: 6/2/2026
#Last Edit: Xehtel on 6/3/2026
#================================================================================================#
#Interpreter: MicroPython
#Tested Micro Controllers: Raspberry Pi Pico W, Raspberry Pi Pico 2 W
#================================================================================================#
#File Dependencies: sysfont.py, st7735_Driver.py
#================================================================================================#

#Imports
import st7735_Driver, time, math
from machine import SPI, Pin, I2C
from st7735_Driver import TFT
from sysfont import sysfont

#Set SPI & TFT Pins and Connections
spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
tft = TFT(spi, 21, 20, 17)

#Initialize, color, and set rotation for tft
tft.initr()
tft.rgb(True)
tft.rotation(3)

#PLACEHOLDER LISTS FOR PRINT TEST
listA = [12.34]
listB = [56.78]

#Display to LCD Screen
def environment_display():
  tft.fill(TFT.BLACK)
  tft.text((0, 0), "Title Text", TFT.YELLOW, sysfont, 1, nowrap=True)
  tft.text((0, 15), "S1 T:{:.2f}C H:{:.2f}%".format(listA[0], listB[0]), TFT.WHITE, sysfont, 1, nowrap=True)
