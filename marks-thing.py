#!/usr/bin/python3

change=[False, True, False, True, False, True, False, True, True, True, True, False, True, False, True, True, True, False, True, True, False, True, True, True, False, False]

used = [[[False for x in range(3)] for y in range(3)] for z in range(3)]


def rotate(direction, whichRotation):
	[x, y, z] = direction
	return [[z, y, -z, -y][whichRotation], [x, z, -x, -z][whichRotation], [y, x, -y, -x][whichRotation]]

def reverse(direction):
	return [-value for value in direction]

def words(direction):
	if direction[0]!=0:
		return 'right' if direction[0]>0 else 'left'
	if direction[1]!=0:
		return 'down' if direction[1]>0 else 'up'
	if direction[2]!=0:
		return 'forward' if direction[2]>0 else 'back'
		

def recurse(depth = 0, position = [0, 0, 0], direction = [1, 0, 0]):
	if depth == 26:
		return True #success
	
	newPosition = [position+direction for position, direction in zip(position, direction)]
	for dimension in range(3):
		if newPosition[dimension] < 0 or newPosition[dimension] == 3:
			return False #failure
	if used[newPosition[0]][newPosition[1]][newPosition[2]]:
		return False #failure
	

	used[newPosition[0]][newPosition[1]][newPosition[2]] = True
	success = False
	if change[depth]:
		for whichRotation in range(4):
			if recurse(depth+1, newPosition, rotate(direction, whichRotation)):
				print('turn towards', words(reverse(direction)), 'please')
				success = True
				break
	else:
		if recurse(depth+1, newPosition, direction):
			print('straight towards', words(reverse(direction)), 'please')
			success = True
	used[newPosition[0]][newPosition[1]][newPosition[2]] = False
	return success

used[0][0][0]=True
recurse()


