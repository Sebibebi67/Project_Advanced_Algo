from lib import *
from validercorde import validerCorde
import random as r
import math as m

from display import *
from period import *

def initCordes(s, tableauDistance):
	for i in range(len(s)):
		l = []
		for j in range(len(s)):
			if (validerCorde([], len(s), i, j)):
				l.append(m.sqrt(m.pow(s[j].x-s[i].x, 2)+m.pow(s[j].y-s[i].y, 2)))
			else:
				l.append(0)
		tableauDistance.append(l)
				
	return tableauDistance


def progDyna(n, s, dist):
	global tableauDistance
	global results

	if n==3:
		if len(results) == 0 or dist<min(results):
			results.append(dist)

	for k in range(0, n):
		dist2 = dist + tableauDistance[s[(k-1)%n]][s[(k+1)%n]]
		s2 = list(s)
		s2.pop(k)
		progDyna(n-1, s2, dist2)

t = 0
i = 4
while t <= 60*2*10**6:
	n = i
	s = [Point(m.cos(2*k*m.pi/n),m.sin(2*k*m.pi/n)) for k in range(n)]
	tableauDistance = []
	tableauDistance = initCordes(s, tableauDistance)
	results = []

	poly = [k for k in range(n)]

	t1 = micro()
	progDyna(n, poly, 0)
	t2 = micro()
	t = t2-t1

	print("\nTaille :",len(s))
	print("Meilleurs resultats :",results[-1],", sur un total de :", len(results))
	print("Durée du calcul : ",displayPeriod(t))

	i+=1