#About: Gathers Data from the HDC3022
#Created: 5/21/2026
#Last Edit: Xehtel on 6/3/2026
#================================================================================================#
#Interpreter: MicroPython
#Tested Micro Controllers: Raspberry Pi Pico W, Raspberry Pi Pico 2 W
#================================================================================================#
#File Dependencies: hdc302x_Driver.py
#================================================================================================#

#Imports
from machine import Pin, I2C
import time
import hdc302x_Driver #Driver Import

#Class Allows Import of All Included Functions
#Designed to Support 1 to 8 HDC3022 Sensors
class HDC3022_Sensor:
    #I2C Buses
    i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000) #I2C Bus 0 (GP1=SCL, GP0=SDA)
    i2c1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000) #I2C Bus 1 (GP3=SCL, GP2=SDA)
    
    sensorList = [
        ("Sensor 1", "x044", hdc302x_Driver.HDC302X(i2c0, address=0x44)), #Sensor 1 on Bus 0
        ("Sensor 2", "x045", hdc302x_Driver.HDC302X(i2c0, address=0x45)), #Sensor 2 on Bus 0
        ("Sensor 3", "x046", hdc302x_Driver.HDC302X(i2c0, address=0x46)), #Sensor 3 on Bus 0
        ("Sensor 4", "x047", hdc302x_Driver.HDC302X(i2c0, address=0x47)), #Sensor 4 on Bus 0
        ("Sensor 5", "x044", hdc302x_Driver.HDC302X(i2c1, address=0x44)), #Sensor 5 on Bus 1
        ("Sensor 6", "x045", hdc302x_Driver.HDC302X(i2c1, address=0x45)), #Sensor 6 on Bus 1
        ("Sensor 7", "x046", hdc302x_Driver.HDC302X(i2c1, address=0x46)), #Sensor 7 on Bus 1
        ("Sensor 8", "x047", hdc302x_Driver.HDC302X(i2c1, address=0x47))] #Sensor 8 on Bus 1

    #Lists All I2C sensorList(name, address, sensor) Data
    timestamps = []
    nameList = [] 
    addrsList = [] 
    tempsList = []  
    humsList = [] 

#=========================================MAIN FUNCTIONS=========================================#

    #Grabs Data from Each Sensor & Sends it to Corresponding Data Lists
    def grab_data():
        #Clear the Lists for Next Iteration of Data
        HDC3022_Sensor.timestamps.clear()
        HDC3022_Sensor.nameList.clear()
        HDC3022_Sensor.addrsList.clear()
        HDC3022_Sensor.tempsList.clear()
        HDC3022_Sensor.humsList.clear()
        #Loops Through an Iteration of Data
        for i, (sensor_name, addrs, sensor) in enumerate(HDC3022_Sensor.sensorList):
            #Try to Grab Sensor Data, Fill with Placeholders if no Sensor
            try:
                #Grabs Sensor Data
                temp = sensor.temperature
                hum = sensor.relative_humidity
                #Appends Sensor Data
                HDC3022_Sensor.nameList.append(sensor_name)
                HDC3022_Sensor.addrsList.append(addrs)
                HDC3022_Sensor.tempsList.append(temp)
                HDC3022_Sensor.humsList.append(hum)
                #Takes Current Timestamp
                now = time.localtime() #To Accurately Timestamp Each Sensor Separately, Must Copy to Each Enumeration of Try/Except
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                #Appends Timestamp
                HDC3022_Sensor.timestamps.append(times)
            except Exception as e:
                #Appends Placeholder Sensor Data
                HDC3022_Sensor.nameList.append(sensor_name)
                HDC3022_Sensor.addrsList.append(addrs)
                HDC3022_Sensor.tempsList.append(0.0)
                HDC3022_Sensor.humsList.append(0.0)
                #Takes Current Timestamp
                now = time.localtime() #To Accurately Timestamp Each Sensor Separately, Must Copy to Each Enumeration of Try/Except
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                #Appends Timestamp
                HDC3022_Sensor.timestamps.append(times)
#=====================================END OF MAIN FUNCTIONS======================================#

    

#=======================================DEBUGGING FUNCTIONS======================================#
#~~~~~~~~~~~~~~~~~~~~~~~~(Functions Should Be Put In Main Loop To Debug)~~~~~~~~~~~~~~~~~~~~~~~~~#

    #Prints the SensorName, SensorAddress, Temperature, Humidity, & the Timestamp
    @staticmethod 
    def debug_readings():        
        #Debug Prints for Bus 0 & Bus 1 (All Sensors on sensorList) 
        print(f"\n================================SENSOR LOGGER================================")
        print(f"---BUS 0---")
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[0], HDC3022_Sensor.addrsList[0], HDC3022_Sensor.tempsList[0], HDC3022_Sensor.humsList[0], HDC3022_Sensor.timestamps[0])) #Bus 0 Sensor 1 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[1], HDC3022_Sensor.addrsList[1], HDC3022_Sensor.tempsList[1], HDC3022_Sensor.humsList[1], HDC3022_Sensor.timestamps[1])) #Bus 0 Sensor 2 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[2], HDC3022_Sensor.addrsList[2], HDC3022_Sensor.tempsList[2], HDC3022_Sensor.humsList[2], HDC3022_Sensor.timestamps[2])) #Bus 0 Sensor 3 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[3], HDC3022_Sensor.addrsList[3], HDC3022_Sensor.tempsList[3], HDC3022_Sensor.humsList[3], HDC3022_Sensor.timestamps[3])) #Bus 0 Sensor 4 Log
        print(f"---BUS 1---")
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[4], HDC3022_Sensor.addrsList[4], HDC3022_Sensor.tempsList[4], HDC3022_Sensor.humsList[4], HDC3022_Sensor.timestamps[4])) #Bus 1 Sensor 5 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[5], HDC3022_Sensor.addrsList[5], HDC3022_Sensor.tempsList[5], HDC3022_Sensor.humsList[5], HDC3022_Sensor.timestamps[5])) #Bus 1 Sensor 6 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[6], HDC3022_Sensor.addrsList[6], HDC3022_Sensor.tempsList[6], HDC3022_Sensor.humsList[6], HDC3022_Sensor.timestamps[6])) #Bus 1 Sensor 7 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(HDC3022_Sensor.nameList[7], HDC3022_Sensor.addrsList[7], HDC3022_Sensor.tempsList[7], HDC3022_Sensor.humsList[7], HDC3022_Sensor.timestamps[7])) #Bus 1 Sensor 8 Log
        time.sleep(1.0) #Functions Print Delay in Seconds
#===================================END OF DEBUGGING FUNCTIONS===================================#
