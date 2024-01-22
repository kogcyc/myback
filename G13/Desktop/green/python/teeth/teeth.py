
from D2 import *
from svgLIB import *
import cairosvg
import sys
import os

def realHYP(l,c):
	a = 360.0/(c*2.0)
	h = (l/2.0) / sin(radians(a))
	return h

def translate_rotate_RAY(ray,x,y,a):
	newRay = []
	for t in ray:
		newPt = D2(t.x,t.y)
		pt = newPt.translate(x,y)
		rt = pt.rotzero(a)
		newRay.append(rt)
	return(newRay)
		
svgMID = ""

tooth_length = 8
tooth_angle = 10
tooth_radius = 7.9375

center = D2()

a2 = center.vector(tooth_radius,360-tooth_angle)
a3 = center.vector(tooth_radius,180+tooth_angle)
a1 = a2.vector(tooth_length,90-tooth_angle)
a4 = a3.vector(tooth_length,90+tooth_angle)

ptray = [a1,a2,a3,a4]

leng = realHYP(12.7,15)

pt_r_ray = translate_rotate_RAY(ray=ptray,x=0,y=0,a=270)

#leng = realHYP(12.7,15)
#tray = transRAY(ptray,leng)

teeth = 15
allray = []
for tooth in range(teeth):
	allray.append(translate_rotate_RAY(ray=pt_r_ray,x=leng,y=0,a=(360.0/teeth)*tooth))

for i in ptray:
	#print(i)
	print(i.x)
	print(i.y)

for i in pt_r_ray:
	#print(i)
	print(i.x)
	print(i.y)

svgMID = svgMID + startPATH(a1)
svgMID = svgMID + pathLINETO(a2)
svgMID = svgMID + pathARCTO(a3,r=tooth_radius,thing="0 0 0")
svgMID = svgMID + pathLINETO(a4)

a5 = a4.vector(30+tooth_length+tooth_radius,250)
svgMID = svgMID + pathLINETO(a5)

a6 = D2(-a5.x,a5.y)
svgMID = svgMID + pathLINETO(a6)

svgMID = svgMID + endPATH(fill="#aaa")





#print(makeSVG(svgMID))

##print(f2.y)

#print(f2.x+c1.x)

ff = open('aaa.svg','w')
ff.write(makeSVG(svgMID))
ff.close()

cairosvg.svg2png(bytestring=makeSVG(svgMID),write_to='aaa.png')



