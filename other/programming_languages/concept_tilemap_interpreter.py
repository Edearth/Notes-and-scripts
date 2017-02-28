# WARNING! This program is a mockup, a proof of concept, it doesn't really work. 
#
# This is an interpreter for a custom programming language in which you can control the
# flow of the interpreter's cursor in a 2-dimensional grid (the text of the file) with 
# 'directional arrows' characters (>, <, ^, v). The idea is not original, it was inspired
# by fungeoid programming languages (http://esolangs.org/wiki/Fungeoid), p called Befunge ( ), although I haven't really tried it.

# TODO:
# · Add multiple threads: with an instruction you could add a new Thread that would interpret
#		the code at the same time as the original thread. Imagine 'spawnThread()' is a function
#		used to spawn a new thread at the second character after the calling of this function.
#		This function would leave the calling thread in the next character after this function
#		and at the same time create a new Thread two characters after the calling. So, take
#		this program as an example:
#
#			> /*code*/ > spawnThread()v> /*thread 2 code*/
#									  > /*thread 1 code*/
#
# 		You could also have them execute the same code simultaneously, as in the following example:
#
#			> /*code*/ > spawnThread()>> /*thread 1 & 2 code*/
#
#		I don't know yet what kind of use this could have, but it would be really cool to
#		make an 'execution viewer' that colors the active threads.

import time

program = '''v
> x+=1; v
 
 
 v      <
 >if(x!=4)v> print(x); exit
^         <
'''

def get(x,y):
	global program
	lines = program.split('\n')
	if y in range(len(lines)):
		if x in range(len(lines[y])):
			return lines[y][x]
	return None

def advance_cursor(cursor):
	if cursor["dir"] is '>':
		cursor["x"] += 1
	elif cursor["dir"] is '<':
		cursor["x"] -= 1
	elif cursor["dir"] is 'v':
		cursor["y"] += 1
	elif cursor["dir"] is '^':
		cursor["y"] -= 1
	return cursor

def read_next_char():
	global cursor
	c = get(cursor["x"],cursor["y"])
	if c is None or c is ' ':
		advance_cursor(cursor)
		return read_next_char()
	elif c in ['v','^','<','>']:
		cursor["dir"] = c
		advance_cursor(cursor)
		return read_next_char()
	else:
		advance_cursor(cursor)
		return c

def execute_command(command):
	global x
	if 'x+=1' in command:
		x = x+1
	elif 'print(x)' in command:
		print(str(x))

def check_condition(condition):
	global x
	if 'x!=4' in condition:
		return x!=4


cursor = {'x':0, 'y':0, 'dir':'>'}

DEBUG = False

buffer = ""
last_command = 0
x = 0

while "exit" != buffer[-4:]:
	readed = read_next_char()
	#operation
	if readed is ";":
		command = buffer[last_command:]
		last_command = len(buffer)
		execute_command(command)
	#condition/function
	elif readed is "(":
		#condition
		if buffer[-2:] == "if":
			buffer += str(readed)
			condition_start = len(buffer)
			while readed != ")":
				readed = read_next_char()
				buffer += str(readed)
			condition = buffer[condition_start:]
			condition_result = check_condition(condition)
			if not condition_result:
				cursor = advance_cursor(cursor)
			readed = read_next_char()

	buffer += str(readed)
	if DEBUG:
		print(readed, end='', flush=True)
		time.sleep(0.01)