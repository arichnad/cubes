#!/usr/bin/python3


cubes = [ \
[[ \
'xxx', \
' x ', \
]],[[ \
'xx ', \
' xx', \
]],[[ \
'xx', \
'x ', \
],[ \
'x ', \
'  ', \
]],[[ \
'xx', \
'x ', \
],[ \
'  ', \
'x ', \
]],[[ \
'xx', \
'x ', \
],[ \
' x', \
'  ', \
]],[[ \
'xx', \
'x ', \
]],[[ \
'xxx', \
'x  ', \
]]]

#cubes = [ \
#[[ \
#'xx ', \
#'xx ', \
#],[ \
#'   ', \
#' xx', \
#]],[[ \
#'xxx', \
#'xx ', \
#'x  ', \
#]],[[ \
#'xxx', \
#'x  ', \
#'x  ', \
#],[ \
#'x  ', \
#'   ', \
#'   ', \
#]],[[ \
#'x ', \
#'x ', \
#],[ \
#'xx', \
#'  ', \
#]],[[ \
#'xxx', \
#'  x', \
#],[ \
#'x  ', \
#'   ', \
#]]]

usedCube = [False for i in range(len(cubes))]

import copy

unfilled = [ \
['xxx','xxx','xxx'], \
['xxx','???','???'], \
['xxx','???','???']]

unfilledOriginal = copy.deepcopy(unfilled)


#damn, python doesn't have multi-line lambdas
#http://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not
def simpleRotateHelper(cube, number, z, y, x, d, h, w):
	rotation = [y, x, h-1-y, w-1-x]
	return cube[z][rotation[number]][rotation[(number+1)%4]]

def simpleRotate(cube, number):
	d, h, w = len(cube), len(cube[0]), len(cube[0][0])
	outW, outH, outD = [w, h][number%2], [h, w][number%2], d
	return [[[simpleRotateHelper(cube, number, z, y, x, outD, outH, outW) for x in range(outW)] for y in range(outH)] for z in range(outD)]

#damn, python doesn't have multi-line lambdas
#http://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not
def offAxisRotateHelper(cube, number, z, y, x, d, h, w):
	rotation = [z, x, d-1-z, w-1-x]
	return cube[rotation[number]][y][rotation[(number+1)%4]]

def offAxisRotate(cube, number):
	d, h, w = len(cube), len(cube[0]), len(cube[0][0])
	outW, outH, outD = [w, d][number%2], h, [d, w][number%2]
	return [[[offAxisRotateHelper(cube, number, z, y, x, outD, outH, outW) for x in range(outW)] for y in range(outH)] for z in range(outD)]

def rotate(cube, top, rotation):
	cube=offAxisRotate(cube, top) if top <= 3 else offAxisRotate(simpleRotate(cube, 1), (top-4)*2+1)
	return simpleRotate(cube, rotation)

#usually returns only one value, until we reach the ?s at the end
def findUnfilled():
	d, h, w = len(unfilled), len(unfilled[0]), len(unfilled[0][0])
	for z in range(d):
		for y in range(h):
			for x in range(w):
				if unfilled[z][y][x] == 'x':
					return [[z, y, x]]

	#ok, we're at the end.  return all of the '?'s
	returnValue = []

	for z in range(d):
		for y in range(h):
			for x in range(w):
				if unfilled[z][y][x] == '?':
					returnValue.append([z, y, x])

	if len(returnValue) > 0:
		return returnValue

	#shouldn't happen?
	return None

def fits(place, position):
	d, h, w = len(position), len(position[0]), len(position[0][0])
	unfilledD, unfilledH, unfilledW = len(unfilled), len(unfilled[0]), len(unfilled[0][0])

	if place[0]+d > unfilledD or place[1]+h > unfilledH or place[2]+w > unfilledW:
		return False
	
	for z in range(d):
		for y in range(h):
			for x in range(w):
				if unfilled[place[0]+z][place[1]+y][place[2]+x] == ' ' and position[z][y][x] == 'x':
					return False
	return True

def placeCube(place, position, newValue = ' '):
	d, h, w = len(position), len(position[0]), len(position[0][0])

	for z in range(d):
		for y in range(h):
			for x in range(w):
				if position[z][y][x] == 'x':
					oldStr = unfilled[place[0]+z][place[1]+y]
					unfilled[place[0]+z][place[1]+y] = oldStr[:place[2]+x] + newValue + oldStr[place[2]+x+1:]

def unplaceCube(place, position):
	d, h, w = len(position), len(position[0]), len(position[0][0])

	for z in range(d):
		for y in range(h):
			for x in range(w):
				if position[z][y][x] == 'x':
					oldStr = unfilled[place[0]+z][place[1]+y]
					unfilled[place[0]+z][place[1]+y] = oldStr[:place[2]+x] + unfilledOriginal[place[0]+z][place[1]+y][place[2]+x] + oldStr[place[2]+x+1:]
	

import sys

def tryPositions(depth = 0):
	if(depth == len(cubes)):
		#success
		return True
	
	#usually returns only one value, until we reach the ?s at the end
	places = findUnfilled()

	for place in places:
		for cube in range(len(cubes)):
			if usedCube[cube]: continue
			usedCube[cube] = True
			for top in range(6):
				for rotation in range(4):
					position = rotate(cubes[cube], top, rotation)
					#if position[0][0][0] == ' ': continue
					if not fits(place, position): continue
					placeCube(place, position)
					if tryPositions(depth + 1):
						print(place, position)
						return True
					unplaceCube(place, position)
			usedCube[cube] = False

	return False



tryPositions()


