from lib import *
from validercorde import validerCorde
import random as r
import math as m

from display import *
from period import *

def initCordes(s, C):
	for i in range(len(s)):
		for j in range(len(s)):
			if (validerCorde([], len(s), i, j)):
				C.append((i, j, m.sqrt(m.pow(s[j].x-s[i].x, 2)+m.pow(s[j].y-s[i].y, 2))))
	return C

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
				dist2 = dist+lenOf(i, j)
				x.append((i,j))
				if (len(x)==len(s)-3 and doNotExist(x,results)):
					results.append((x, dist2))
				else:
					essaisSuccessifs2(x, dist2)


def essaisSuccessifs2AvecElagage(c, dist):
	global results

	for i in range(len(s)):
		for j in range(len(s)):
			#print(i,j)
			if validerCorde(c,len(s),i,j):
				x = list(c)
				dist2 = dist+lenOf(i, j)
				x.append((i,j))
				if (isShorter(results, dist2)): #To use to find the best
					if (len(x)==len(s)-3 and doNotExist(x,results)):
						results.append((x, dist2))
					essaisSuccessifs2AvecElagage(x, dist2)

t = 0
i = 4
while t <= 60*2*10**6:
	n = i
	s = [Point(m.cos(2*k*m.pi/n),m.sin(2*k*m.pi/n)) for k in range(n)]
	C = []
	C = initCordes(s, C)
	results = []
	c = []

	print(len(s))

	t1 = micro()
	essaisSuccessifs2AvecElagage(c, 0)
	t2 = micro()
	t = t2-t1

	print("Meilleurs resultats :",results[-1],", sur un total de :", len(results))
	print("Durée du calcul : ",displayPeriod(t))
	#display(s)

	i+=1
