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
	if row.find('S')!=-1: startPosition = (row.find('S'), rowNumber, 0, 0)
	if row.find('T')!=-1: endPosition = (row.find('T'), rowNumber, 0, 0)

#breadth first search, please

queue=[(startPosition, [])]
seen=set()

def append(newState, moves, newMove):
	x, y, dx, dy = newState
	if newState in seen or not 0<=x<len(board[0])-dx or not 0<=y<len(board)-dy or board[y][x]=='-' or board[y+dy][x+dx] == '-': return
	#the reason we wait to add to moves until here is for performance reasons:
	moves = moves + [newMove]
	seen.add(newState)
	queue.append((newState, moves))
	if newState == endPosition:
		print(moves)
		return True

while len(queue) > 0:
	(x, y, dx, dy), moves = queue.pop(0);dz=1-dx-dy

	if append((x+dx+1, y, dz, dy), moves, 'right') or \
		append((x-dz-1, y, dz, dy), moves, 'left') or \
		append((x, y+dy+1, dx, dz), moves, 'down') or \
		append((x, y-dz-1, dx, dz), moves, 'up'):
		break

