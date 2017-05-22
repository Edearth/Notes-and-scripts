# INFO: This script requires LibreOffice to be installed in the system
# REMINDER: It'd be nice to be able to pass the LibreOffice installation path through
#           the console parameters.

import os
import subprocess

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	print(f)
	if(".xlsx" in f or ".xlsx" in f):
		subprocess.run(["C:\Program Files (x86)\LibreOffice 5\program\soffice", "--headless", "--convert-to", "csv", f])