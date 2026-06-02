#About: Displays Text to an LCD
#Created: 6/2/2026
#Last Edit: Xehtel on 6/2/2026
#================================================================================================#
#Requires: sysfont.py & st7735_Driver.py
#Interpreter: MicroPython
#Tested Micro Controllers: Raspberry Pi Pico W, Raspberry Pi Pico 2 W
#================================================================================================#

#Imports
import st7735, time, math
from machine import SPI, Pin, I2C
from st7735 import TFT
from sysfont import sysfont

#Set SPI & TFT Pins and Connections
spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
tft = TFT(spi, 21, 20, 17)

#Initialize, color, and set rotation for tft
tft.initr()
tft.rgb(True)
tft.rotation(3)

def environment_display():
  tft.fill(TFT.BLACK)

  tft.text((0, 0), "ENV MONITOR", TFT.YELLOW, sysfont, 1, nowrap=True)

  tft.text((0, 15), "S1 T:{:.2f}C H:{:.2f}%".format(listA[0], listB[0]), TFT.WHITE, sysfont, 1, nowrap=True)
  tft.text((0, 30), "S2 T:{:.2f}C H:{:.2f}%".format(listA[1], listB[1]), TFT.WHITE, sysfont, 1, nowrap=True)
  tft.text((0, 45), "S3 T:{:.2f}C H:{:.2f}%".format(listA[2], listB[2]), TFT.WHITE, sysfont, 1, nowrap=True)
