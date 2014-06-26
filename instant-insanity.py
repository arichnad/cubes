#!/usr/bin/python3


inputCubes = ['rrrgwb', 'wwbgrg', 'bbwrgg', 'rrbwwg']
cubes = inputCubes[:]

def simpleRotate(cube, number):
	return cube[number:4] + cube[0:number] + cube[4:6]

def offAxisRotate(cube, number):
	offAxis = [1, 5, 3, 4]
	return cube[0] + cube[offAxis[number]] + cube[2] + cube[offAxis[(number+2)%4]] + cube[offAxis[(number+3)%4]] + cube[offAxis[(number+1)%4]]

def rotate(cube, top, rotation):
	cube=offAxisRotate(cube, top) if top <= 3 else offAxisRotate(simpleRotate(cube, 1), (top-4)*2+1)
	return simpleRotate(cube, rotation)

def checkCorrectness(depth):
	for i in range(depth):
		for j in range(i):
			for k in [0, 2, 4, 5]:
				if cubes[i][k] == cubes[j][k]:
					#fail
					return False
	
	#so far so good
	return True


def tryPositions(depth = 0):
	if not checkCorrectness(depth): return
	
	if depth == len(cubes):
		#success!
		print(cubes)
		return
	
	for top in range(6):
		for rotation in range(4):
			cubes[depth] = rotate(inputCubes[depth], top, rotation)
			tryPositions(depth+1)

tryPositions()

