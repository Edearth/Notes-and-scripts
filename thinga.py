#0: nothing
#1: conductor (OFF)
#2: conductor (ON): if there are off conductors or machines touching it, it powers them up
#3: generator: if there are off conductors or machines touching it, it powers them up
#8: machine (OFF)
#9: machine (ON): game ends when it's ON

#Add flips and switches, current alternators and things

world = [
[3,0,1,1,1],
[1,0,1,0,1],
[1,1,1,0,8],
]

world_tmp = [
[3,0,1,1,1],
[1,0,1,0,1],
[1,1,1,0,8],
]

def drawScreen():
	global world, counter
	print("Turn: "+str(counter))
	screen_batch = ""
	for row in world:
		screen_batch += " "
		for cell in row:
			screen_batch += str(cell)
		screen_batch += "\n"
	screen_batch += "-"*(len(world[0])+2)

	print(screen_batch)

def getNeighbouring(x,y,value):
	global world, world_tmp
	
	lista = []
	try :
		if world[y-1][x] == value and y-1 >= 0:
			lista.append((y-1,x))
	except IndexError:
		pass
	try :
		if world[y+1][x] == value:
			lista.append((y+1,x))
	except IndexError:
		pass
	try :
		if world[y][x-1] == value and x-1 >= 0:
			lista.append((y,x-1))
	except IndexError:
		pass
	try :
		if world[y][x+1] == value:
			lista.append((y,x+1))
	except IndexError:
		pass

	#DEBUG
	#print("neighbouring "+str(value)+" for "+str(x)+","+str(y)+": "+str(len(lista)))
	#print(str(lista))
	return lista

def copyWorld():
	global world, world_tmp
	for y, row in enumerate(world):
		for x, cell in enumerate(row):
			world_tmp[y][x] = cell

def decopyWorld():
	global world, world_tmp
	for y, row in enumerate(world_tmp):
		for x, cell in enumerate(row):
			world[y][x] = cell

def litNeighbouring(x,y,val):
	global world_tmp, stop, won
	neighbourCables = getNeighbouring(x,y,val)
	for cable in neighbourCables:
		world_tmp[cable[0]][cable[1]] = val+1
		if val == 8:
			stop = True
			won = True

def update():
	global world, world_tmp, stop, won, counter
	copyWorld()
	counter += 1
	for y, row in enumerate(world):
		for x, cell in enumerate(row):
			if(cell == 3):
				litNeighbouring(x,y,1)
				litNeighbouring(x,y,8)
			if(cell == 2):
				litNeighbouring(x,y,1)
				litNeighbouring(x,y,8)
	decopyWorld()

counter = 0
won = False
stop = False

drawScreen()
while not stop:
	update()
	drawScreen()
	if counter > 9:
		stop = True
if won:
	print("WINNER!")