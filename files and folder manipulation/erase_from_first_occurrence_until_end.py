# This script will find all the files in a directory and see if they contain a string of
# characters. If that's true, it will then erase everything from the first occurrence of
# that string until the end of the file.
# This was used to crop all remainding html from downloaded files that appeared to be
# corrupted just because the server was appending html code at the end of those files.

# REMINDER: It'd be nice to pass the string as a parameter.
#           Also separating the "do to all" logic and the "erasing" logic would be useful.
#               Preferably, I'd like to be able to use a script "apply_to_all" and then
#               pass this script with its arguments and so as arguments for the other script. 

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