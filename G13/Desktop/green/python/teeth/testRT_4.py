
from sys import argv
from D2 import *
from svgLIBmm import *
import cairosvg

def fakeHYP(l,c):
	a = float(l)*c
	b = a / 6.283185307179586 # 2 pi
	return b

def realHYP(l,c):
	a = 360.0/(c*2.0)
	h = (l/2.0) / sin(radians(a))
	return h

tooth_length = 2.0
tooth_angle = 22.0
roller_radius = (5/32.0)*25.4

try:
	teeth = int(argv[1])
except:
	teeth = 15

print(360.0/teeth/4)

a2 = D2().vector(roller_radius,270-tooth_angle)
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
	tooth_rounded_array = [x.round2() for x in tooth_rotated_array]
	full_array.append(tooth_rounded_array)

svgMID = startPATH(full_array[teeth-1][3])

for x in full_array:
	svgMID = svgMID + pathLINETO(x[0])
	svgMID = svgMID + pathLINETO(x[1])
	svgMID = svgMID + pathARCTO(x[2],r=roller_radius,thing="0 0 0")
	svgMID = svgMID + pathLINETO(x[3])

svgMID = svgMID + endPATH(fill="#000")

ff = open('teeth.svg','w')
ff.write(makeSVG(svgMID))
ff.close()

#cairosvg.svg2png(bytestring=makeSVG(svgMID),write_to='teeth.png')


