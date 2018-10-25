#!/usr/bin/python3

board=[
'oooo',
'oooo',
'o#oo',
'oooo'
]

for rowNumber, row in enumerate(board):
	if row.find('#') != -1:
		endY=rowNumber
		endX=row.find('#')

startPosition=(0,0,0,0,1)

#breadth first search, please

queue=[(startPosition, [])]
seen=set()

def append(queue, seen, newState, moves):
	if newState in seen: return
	x, y, dx, dy, dz = newState
	if x<0 or y<0 or x==len(board[0]) or y==len(board): return
	if dz == 1 and x == endX and y == endY: print(moves)
	seen.add(newState)
	queue.append((newState, moves))

while len(queue) > 0:
	(x, y, dx, dy, dz), moves = queue.pop(0)

	#rotate across y axis
	append(queue, seen, (x+(dx+dy), y, dz, dy, dx), moves + ['right'])
	append(queue, seen, (x-(dy+dz), y, dz, dy, dx), moves + ['left'])

	#rotate across x axis
	append(queue, seen, (x, y+(dx+dy), dx, dz, dy), moves + ['down'])
	append(queue, seen, (x, y-(dy+dz), dx, dz, dy), moves + ['up'])

