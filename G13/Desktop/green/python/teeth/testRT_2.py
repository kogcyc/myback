
from sys import argv
from math import *
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

def rotateRAY(ray,angle):
	returnRAY = []
	for pt in ray:
		newPT = pt.rotzero(angle)
		returnRAY.append(newPT)
	return returnRAY
		
def translateRAY(ray,x,y):
	returnRAY = []
	for pt in ray:
		newPT = pt.translate(x,y)
		returnRAY.append(newPT)
	return returnRAY

tooth_length = 2
tooth_angle = 22
tooth_radius = 7.9375/2.0
try:
	teeth = int(argv[1])
except:
	teeth = 15

center = D2()

a2 = center.vector(tooth_radius,360-tooth_angle)
a3 = center.vector(tooth_radius,180+tooth_angle)
a1 = a2.vector(tooth_length,90-tooth_angle)
a4 = a3.vector(tooth_length,90+tooth_angle)



#a1 = D2(10,-20)
#a2 = D2(10,40)
#a3 = D2(-10,40)
#a4 = D2(-10,-20)

ptray = [a1,a2,a3,a4]

leng = fakeHYP(12.7,teeth)
print(leng)

rotated_ray = rotateRAY(ptray,-90)

translated_array = translateRAY(rotated_ray,leng,0)


full_array = []

for tooth in range(teeth):
	angle = (360.0 / teeth) * tooth
	tooth_rotated_array = rotateRAY(translated_array,angle)
	for pt in tooth_rotated_array:
		full_array.append(pt)


rrray = [x.rotzero(0) for x in full_array]
full_array = rrray


#for point in ptray:
	#print(f'{point.x} : {point.y}')

#print("\n---------------------------\n")

#for point in rotated_ray:
	#print(f'{point.x} : {point.y}')

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



#a5 = a4.vector(30+tooth_length+tooth_radius,250)
#svgMID = svgMID + pathLINETO(a5)

#a6 = D2(-a5.x,a5.y)
#svgMID = svgMID + pathLINETO(a6)

#svgMID = svgMID + endPATH(fill="#f00",fillo=1.0)

#svgMID = svgMID + startPATH(a1)
#svgMID = svgMID + pathLINETO(a2)
#svgMID = svgMID + pathLINETO(a3)
#svgMID = svgMID + pathLINETO(a4)
#svgMID = svgMID + endPATH(fill="#faa")


#svgMID = svgMID + makeCIRCLE(D2(),tooth_radius,fillo=1.0)


ff = open('teeth.svg','w')
ff.write(makeSVG(svgMID))
ff.close()


#cairosvg.svg2png(bytestring=makeSVG(svgMID),write_to='teeth.png')


