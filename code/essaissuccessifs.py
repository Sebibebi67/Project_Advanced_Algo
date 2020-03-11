from lib import *
from validercorde import validerCorde
import random as r

s = [Point(-9,3), Point(-2,5), Point(0,4), Point(1,1), Point(-1,-2), Point(-4,-4), Point(-9,-1), Point(-10,1)]

def essaisSuccessifs():
	c = []
	for i in range(len(s)):
		possible = []
		for j in range(len(s)):
			if validerCorde(c,i,j):
				possible.append((i,j))
		if len(possible)>0:
			c.append(possible[r.randint(0,len(possible)-1)])
		possible = []
	return c

print(essaisSuccessifs())