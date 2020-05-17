# This script counts all the lines in files from the folder it was
# executed on and its subfolders.

import os
import sys


def countLinesSubfolders(extension, verbose):
	total_lines = 0

	for path, subdirs, files in os.walk("."):
		for name in files:
			f = os.path.join(path, name)
			if(extension == '*' or ("."+extension) in f):
				with open(f) as file:
					for i, l in enumerate(file):
						pass
					lines = i + 1

					total_lines = total_lines + lines
					if(verbose):
						print("Lines in "+'{0: <40}'.format(f+": ")+'{0: <6}'.format(str(lines))+"Accumulated lines: "+'{0: <8}'.format(str(total_lines)))
	if (verbose):
		print("")
	print("Total lines:"+str(total_lines))


if __name__ == "__main__":
	if (len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] not in ["-v", "--verbose"]) ):
		print("Usage: "+sys.argv[0]+" [-v|--verbose]")
	else:
		verbose = False
		if (len(sys.argv) == 2 != None and sys.argv[1] in ["-v", "--verbose"]):
			verbose = True
		extension = "java"
		countLinesSubfolders(extension, verbose)