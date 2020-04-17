from lib import *
from validercorde import validerCorde
import random as r
import math as m

from display import *
from period import *

s = [Point(0,0), Point(2,1), Point(3,2),Point(4,4), Point(4,5), Point(3,7), Point(2,8)]#, Point(0,9), Point(-1,9), Point(-3,8), Point(-4,7), Point(-5,5), Point(-5,4), Point(-4,2), Point(-3,1), Point(-1,0)

C = []

def initCordes(s, C):
	for i in range(len(s)):
		for j in range(len(s)):
			if (validerCorde([], len(s), i, j)):
				C.append((i, j, m.sqrt(m.pow(s[j].x-s[i].x, 2)+m.pow(s[j].y-s[i].y, 2))))
	return C

C = initCordes(s, C)
#print(C, len(C))

results = []

c = []

def doNotExist(a, la):
	sa = set()
	for e in a:
		sa.add(frozenset((e[0], e[1])))
	for e in [l[0] for l in la]:
		se = set()
		for c in e:
			se.add(frozenset((c[0], c[1])))
		if (se == sa):
			return False
	return True

def isShorter(results, dist):
	if len(results) == 0:
		return True
	minimum = min([r[1] for r in results])
	if (dist < minimum):
		return True
	return False

def lenOf(i,j):
	global C
	for c in C:
		if i == c[0] and j == c[1]:
			return c[2]

def essaisSuccessifs2(c, dist):
	global results

	for i in range(len(s)):
		for j in range(len(s)):
			#print(i,j)
			if validerCorde(c,len(s),i,j):
				x = list(c)
				dist += lenOf(i, j)
				x.append((i,j))
				#if (isShorter(results, dist)): #To use to find the best
				if (len(x)==len(s)-3 and doNotExist(x,results)):
					results.append((x, dist))
				else:
					essaisSuccessifs2(x, dist)

t1 = micro()
essaisSuccessifs2(c, 0)
t2 = micro()
print(results,len(results))
print("Durée du calcul : ",displayPeriod(t2-t1))

#for i in range(10):
#	a = essaisSuccessifs()
#	print(a)
#	if (len(a)==len(s)-3):
#		print("On obtient une triangulation valide !")
#	else:
#		print("On obtient une triangulation non valide !")
#	displayWithCorde(s,a)


