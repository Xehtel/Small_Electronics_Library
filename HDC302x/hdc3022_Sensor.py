#About: Gathers Data from the HDC3022
#Created: 5/21/2026
#Last Edit: Xehtel on 6/1/2026
#================================================================================================#
#Requires: hdc302x_AdafruitDriver.py
#Interpreter: MicroPython
#Tested Micro Controllers: Raspberry Pi Pico W, Raspberry Pi Pico 2 W
#================================================================================================#

#Imports
from machine import Pin, I2C
import time
import hdc302x_AdafruitDriver #Driver Import

#Class Allows Import of All Included Functions
class HDC3022_Sensor:
    #I2C Buses
    i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000) #I2C Bus 0 (GP1=SCL, GP0=SDA)
    i2c1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000) #I2C Bus 1 (GP3=SCL, GP2=SDA)
    
    sensorList = [
        ("Sensor 1", "x044", hdc302x_AdafruitDriver.HDC302X(i2c0, address=0x44)), #Sensor 1 on Bus 0
        ("Sensor 2", "x045", hdc302x_AdafruitDriver.HDC302X(i2c0, address=0x45)), #Sensor 2 on Bus 0
        ("Sensor 3", "x046", hdc302x_AdafruitDriver.HDC302X(i2c0, address=0x46)), #Sensor 3 on Bus 0
        ("Sensor 4", "x047", hdc302x_AdafruitDriver.HDC302X(i2c0, address=0x47)), #Sensor 4 on Bus 0
        ("Sensor 5", "x044", hdc302x_AdafruitDriver.HDC302X(i2c1, address=0x44)), #Sensor 5 on Bus 1
        ("Sensor 6", "x045", hdc302x_AdafruitDriver.HDC302X(i2c1, address=0x45)), #Sensor 6 on Bus 1
        ("Sensor 7", "x046", hdc302x_AdafruitDriver.HDC302X(i2c1, address=0x46)), #Sensor 7 on Bus 1
        ("Sensor 8", "x047", hdc302x_AdafruitDriver.HDC302X(i2c1, address=0x47))] #Sensor 8 on Bus 1

  
#=======================================DEBUGGING FUNCTIONS======================================#
#~~~~~~~~~~~~~~~~~~~~~~~~(Functions Should Be Put In Main Loop To Debug)~~~~~~~~~~~~~~~~~~~~~~~~~#

    #Basic Reading Supporting 1 to 8 HDC3022 Sensors & Prints the SensorName, SensorAddress, Temperature, Humidity, & the Timestamp
    @staticmethod 
    def debug_readings():
    #Debug Data for sensorList Print
        timestamps = [] #Lists all I2C Sensors Timestamps for Print Statements
        nameList = [] #Lists Sensor Names for Print Statements
        addrsList = [] #Lists Sensor Addresses for Print Statements
        tempsList = [] #Lists Sensor Temperatures for Print Statements
        humsList = [] #Lists Bus 0 Humidities Names for Print Statements
        for i, (sensor_name, addrs, sensor) in enumerate(HDC302X_Sensors.sensorList):
            try:
                #Grabs Sensor Data
                temp = sensor.temperature
                hum = sensor.relative_humidity
                #Appends Sensor Data
                nameList.append(sensor_name)
                addrsList.append(addrs)
                tempsList.append(temp)
                humsList.append(hum)
                #Takes Current Timestamp
                now = time.localtime() 
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                #Appends Timestamp
                timestamps.append(times)
            except Exception as e:
                #Appends Placeholder Sensor Data
                nameList.append(sensor_name)
                addrsList.append(addrs)
                tempsList.append(0.0)
                humsList.append(0.0)
                #Takes Current Timestamp
                now = time.localtime() 
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                #Appends Timestamp
                timestamps.append(times)
        
        #Debug Prints for Bus 0 & Bus 1 (All Sensors on sensorList) 
        print(f"\n================================SENSOR LOGGER================================")
        print(f"---BUS 0---")
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[0], addrsList[0], tempsList[0], humsList[0], timestamps[0])) #Bus 0 Sensor 1 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[1], addrsList[1], tempsList[1], humsList[1], timestamps[1])) #Bus 0 Sensor 2 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[2], addrsList[2], tempsList[2], humsList[2], timestamps[2])) #Bus 0 Sensor 3 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[3], addrsList[3], tempsList[3], humsList[3], timestamps[3])) #Bus 0 Sensor 4 Log
        print(f"---BUS 1---")
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[4], addrsList[4], tempsList[4], humsList[4], timestamps[4])) #Bus 1 Sensor 5 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[5], addrsList[5], tempsList[5], humsList[5], timestamps[5])) #Bus 1 Sensor 6 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[6], addrsList[6], tempsList[6], humsList[6], timestamps[6])) #Bus 1 Sensor 7 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(nameList[7], addrsList[7], tempsList[7], humsList[7], timestamps[7])) #Bus 1 Sensor 8 Log
        time.sleep(1.0) #Functions Print Delay in Seconds
#===================================END OF DEBUGGING FUNCTIONS===================================#
