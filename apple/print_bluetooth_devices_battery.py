# This script can be used to print the remaining battery of devices connected 
# to a MacBook. I used it in my rc/profile config file to quickly (and
# graphically) get a glance at how much battery my devices have left. 
# You can't use that stupid "Magic Mouse" while charging it.
#
# It uses the "ioreg" command line tool to get the information it needs, so
# it should run "out of the box" in a Mac (although this is using Python 2,
# so bear that in mind; probably should update it).

import sys
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

def getColorForBatteryPercent(batteryPercent):
	if(batteryPercent >= 70):
		return GREEN
	elif (batteryPercent >= 30):
		return YELLOW
	else:
		return RED

def formatBatteryPercent(batteryPercent):
	#bar number correction
	if batteryPercent < 100:
		batteryPercent = batteryPercent - 1 #this is done for aesthetical purposes: this way we don't have 10% battery with "2 bars being drawn"
	
	color = getColorForBatteryPercent(batteryPercent)	

	return "["+color+"/"+("/"*(batteryPercent/10)).ljust(10,'.')+ENDC+"] "+color+str(batteryPercent)+"%"+ENDC

def main(argv):
	data = getBatteryDataFromCommandLine()
	devices = splitResultIntoDevices(data)

	for device in devices:
		name = getDeviceName(device)
		battery = getDeviceBatteryPercent(device)
		
		if name != None and name != "" and battery != None and battery != -1:
			print "  - "+(name+": ").ljust(36, ' ')+formatBatteryPercent(battery)

if __name__ == "__main__":
    main(sys.argv)

