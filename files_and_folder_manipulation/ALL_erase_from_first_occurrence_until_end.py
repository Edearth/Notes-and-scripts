import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if(".xlsx" in f):
		print("Repairing file "+f+" ... ")
		file = open(f,  mode="rb+") #errors="ignore",
		error_pos = file.read().find(b'<div id="ydtb-toolbar"')
		if(error_pos > 0):
			print("Correcting error")
			file.seek(error_pos)
			file.truncate()
		else:
			print("No errors found.")