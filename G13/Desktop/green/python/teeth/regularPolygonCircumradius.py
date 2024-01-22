from math import pi, sin
def regPolygonCircumradius(lateralLength,numLaterals): # for bicycle sprockets, the arguements are: (12.7,# of teeth)
	a = pi/numLaterals
	return (lateralLength/float(2)) / sin(a)

