#!/usr/bin/python3

board=[
'ooo-------',
'oSoooo----',
'ooooooooo-',
'-ooooooooo',
'-----ooToo',
'------ooo-',
]
#board=['o'*400]*400
#board[0]='S'+board[0][1:]
#board[-1]=board[-1][:-1]+'T'

for rowNumber, row in enumerate(board):
	if row.find('T') != -1: endPosition = (row.find('T'), rowNumber, 0, 0, 1)
	if row.find('S') != -1: startPosition = (row.find('S'), rowNumber, 0, 0, 1)

#breadth first search, please

queue=[(startPosition, [])]
seen=set()

def append(queue, seen, newState, moves, newMove):
	if newState in seen: return
	x, y, dx, dy, dz = newState
	if x<0 or y<0 or x+dx>=len(board[0]) or y+dy>=len(board): return
	if board[y][x]=='-' or board[y+dy][x+dx] == '-': return
	#the reason we wait to add to moves until here is for performance reasons:
	moves = moves + [newMove]
	if newState == endPosition:
		print(moves)
		return True
	seen.add(newState)
	queue.append((newState, moves))

while len(queue) > 0:
	(x, y, dx, dy, dz), moves = queue.pop(0)

	if append(queue, seen, (x+(dx*2+dy+dz), y, dz, dy, dx), moves, 'right') or \
		append(queue, seen, (x-(dz*2+dy+dx), y, dz, dy, dx), moves, 'left') or \
		append(queue, seen, (x, y+(dy*2+dx+dz), dx, dz, dy), moves, 'down') or \
		append(queue, seen, (x, y-(dz*2+dy+dx), dx, dz, dy), moves, 'up'):
		break

