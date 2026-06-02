# Small Electronics Library | README.md

## GENERAL INSTRUCTIONS

A list of general instructions based on the steps I used to setup each small electronic.

Once all necessary files are on a microcontroller or in a project folder, functions can be called upon in a main.py to start testing your setup.

*Note: More or less setup may be required depending on your personal setup.

### General Documentation

Raspberry Pi Pico W Datasheet [^1]

### HDC302x Folder

You will need to install the hdc302x_AdafruitDriver.py file to use anything in this folder. <br>
GitHub to HDC302x Drivers: [^2]

If using HDC3022, install hdc3022_Sensor.py file. <br>
Once you have installed the required Driver and Sensor file drag them into a microcontroller or project folder along with a main.py file.

### LCD Folder

You will need to install sysfont.py & st7735_Driver.py to use anything in this folder. <br>
GitHub to ST7735 Drivers: [^3]
GitHub to sysfont: [^4]

___
[^1]: https://pip-assets.raspberrypi.com/categories/686-raspberry-pi-pico-w/documents/RP-008312-DS-1-pico-w-datasheet.pdf
[^2]: https://github.com/adafruit/Adafruit_CircuitPython_HDC302x
[^3]: https://github.com/boochow/MicroPython-ST7735/tree/master
[^4]: https://github.com/cheungbx/st7735-esp8266-micropython/tree/master
