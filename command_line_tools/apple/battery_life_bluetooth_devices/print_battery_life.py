#This script can be used to print the battery percentage of devices connected to a MacBook.
#It uses the "ioreg" command line tool to list the devices and lists the devices with both a name and a battery percent.

import re
import subprocess

#ANSI colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

def getBatteryDataFromCommandLine():
	return subprocess.check_output(["ioreg", "-c", "AppleDeviceManagementHIDEventService", "-r", "-l"])

def splitResultIntoDevices(data):
	return re.split('\+\-o.*?<.*?>', data)

def getDeviceName(device):
	match = re.search('"Product" = "(.*?)"', device)
	if match:
		return match.group(1) 
	return ""

def getDeviceBatteryPercent(device):
	match = re.search('"BatteryPercent" = (\d{1,3})', device)
	if match:
		return int(match.group(1))
	return -1

def formatBatteryPercent(batteryPercent):
	#bar number correction
	if batteryPercent < 100:
		batteryPercent = batteryPercent - 1 #this is done for aesthetical purposes: this way we don't have 10% battery with "2 bars being drawn"
	
	#set color
	if(batteryPercent >= 70):
		color = GREEN
	elif (batteryPercent >= 30):
		color = YELLOW
	else:
		color = RED

	#return result
	return color+"/"+("/"*(batteryPercent/10)).ljust(10,'.')+ENDC

data = getBatteryDataFromCommandLine()
devices = splitResultIntoDevices(data)

for device in devices:
	name = getDeviceName(device)
	battery = getDeviceBatteryPercent(device)
	
	if name != None and name != "" and battery != None and battery != -1:
		print "  - "+(name+": ").ljust(36, ' ')+"["+formatBatteryPercent(battery)+"]"
