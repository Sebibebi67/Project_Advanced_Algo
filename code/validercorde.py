from lib import *

s = [Point(-9,3), Point(-2,5), Point(0,4), Point(1,1), Point(-1,-2), Point(-4,-4), Point(-9,-1), Point(-10,1)]

#Hexagone 0,7
c = [(2,6)]

def exist(i,j):
	return (i,j) in c or (j,i) in c

def intersectionCorde(a,b,c,d):
	min1 = min(a,b)
	max1 = max(a,b)

	min2 = min(c,d)
	max2 = max(c,d)

	return (min1 < min2 and min2 < max1 and max1 < max2) or (min2 < min1 and min1 < max2 and max2 < max1)

def coupe(i,j):
	for k in range(len(c)):
		if intersectionCorde(i,j,c[k][0],c[k][1]):
			return True
	return False

def verifCorde(i,j):
	return not exist(i,j) and not coupe(i,j)


#print(verifCorde(5,1))