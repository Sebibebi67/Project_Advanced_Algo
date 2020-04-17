#===============================================
#
#   Class declaration
#
#================================================

class Point:
	"Point class"
	def __init__(self,x = 0,y = 0):
		self.x = x
		self.y = y
		
	def __str__(self):
		return self.toString()

	def toString(self):
		return "("+str(self.x)+","+str(self.y)+")"

#class Segment:
#	"Segment class"
#	def __init__(self,a = Point(0,0),b = Point(0,0)):
#		self.a = a
#		self.b = b

class Rope:
	"Roep class"
	def __init__(self,a = 0,b = 0, length=0):
		self.a = a
		self.b = b
		self.length = length
