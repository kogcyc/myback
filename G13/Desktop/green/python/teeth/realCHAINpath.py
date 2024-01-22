from math import *

def realHYP(l,c):
	a = 360.0/(c*2.0)
	h = (l/2.0) / sin(radians(a))
	return h

def other(l,c):
	h = ((float(l) * float(c)) / pi) / 2.0
	return h
	
