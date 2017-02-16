#REMINDER: It'd be great if you could pass the newline and cell delimiter characters
#          as parameters from the console.

import csv
import sys

def main(argv):
	csvfile = argv[0]
	with open(csvfile) as csvfileh:
		reader = csv.DictReader(csvfileh)
		list_reader = list(reader)

		#print(list_reader[0])
		for i, row in enumerate(list_reader):
			print ("Line "+str(i)+": "+str(row)+"\n")


if __name__ == "__main__":
	if (len(sys.argv) <= 1 or len(sys.argv) > 2):
		print("Usage: "+sys.argv[0]+" file")
	else:
		main(sys.argv[1:])
