
from sys import argv
from math import pi
from D2 import *
from svgLIBmm import *
import cairosvg

def fakeHYP(l,c):
	a = float(l)*c
	b = a / (pi*2)
	return b

def realHYP(l,c):
	a = 360.0/(c*2.0)
	h = (l/2.0) / sin(radians(a))
	return h

tooth_length = 2
tooth_angle = 22
tooth_radius = (5/32.0)*25.4

try:
	teeth = int(argv[1])
except:
	teeth = 15

a2 = D2().vector(tooth_radius,270-tooth_angle)
a1 = a2.vector(tooth_length,360-tooth_angle)
a3 = a2.mirror_x()
a4 = a1.mirror_x()

ptray = [a1,a2,a3,a4]

leng = fakeHYP(12.7,teeth)

translated_array = [x.translate(leng,0) for x in ptray]

full_array = []
for tooth in range(teeth):
	angle = (360.0 / teeth) * tooth
	tooth_rotated_array = [x.rotzero(angle) for x in translated_array]
	full_array = full_array + tooth_rotated_array

svgMID = ""
count = 0
svgMID = svgMID + startPATH(full_array[count])

for tooth in range(teeth-1):
	count = count + 1
	a1 = full_array[count]
	count = count + 1
	a2 = full_array[count]
	count = count + 1
	a3 = full_array[count]
	count = count + 1
	a4 = full_array[count]
	svgMID = svgMID + pathLINETO(a1)
	svgMID = svgMID + pathARCTO(a2,r=tooth_radius,thing="0 0 0")
	svgMID = svgMID + pathLINETO(a3)
	svgMID = svgMID + pathLINETO(a4)

count = count + 1
a1 = full_array[count]
svgMID = svgMID + pathLINETO(a1)
count = count + 1
a2 = full_array[count]
svgMID = svgMID + pathARCTO(a2,r=tooth_radius,thing="0 0 0")
count = count + 1
a3 = full_array[count]
svgMID = svgMID + pathLINETO(a3)
count = count + 1
svgMID = svgMID + endPATH(fill="#000")

ff = open('teeth.svg','w')
ff.write(makeSVG(svgMID))
ff.close()


#cairosvg.svg2png(bytestring=makeSVG(svgMID),write_to='teeth.png')


