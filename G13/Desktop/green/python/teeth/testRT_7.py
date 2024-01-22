
from sys import argv
from D2 import *
from svgLIBmm import *
import math
#import cairosvg

def roller_center_radius(N=3, side_length=12.7): # side length == 'chain pitch' == 12.7mm == 1/2"

	# the shape of a chain on a sprocket is that of a polygon, not a circle (even though the two are nearly the same)    
	# Calculate the distance to the vertex of a polygon given the number of sides and the length of a side
	return side_length / (2 * math.sin(math.pi / N))

def makeSPROCKET(teeth):

	tooth_length = 4.0
	tooth_angle = 360.0 / (teeth)
	roller_radius = (5/32.0)*25.4

	#try:
		#teeth = int(argv[1])
	#except:
		#teeth = 15

	print(360.0/teeth/4)

	a2 = D2().vector(roller_radius,270-tooth_angle)
	a1 = a2.vector(tooth_length,360-tooth_angle)
	a3 = a2.mirror_x()
	a4 = a1.mirror_x()

	ptray = [a1,a2,a3,a4]

	leng = roller_center_radius(teeth)

	translated_array = [x.translate(leng,0) for x in ptray]

	full_array = []
	for tooth in range(teeth):
		angle = (360.0 / teeth) * tooth
		tooth_rotated_array = [x.rotzero(angle) for x in translated_array]
		tooth_rounded_array = [x.round2() for x in tooth_rotated_array]
		full_array.append(tooth_rounded_array)

	svgMID = startPATH(full_array[teeth-1][3])
	lastPT = full_array[teeth-1][3]

	midRAY = []

	for x in full_array:
		#midRAY.append(lastPT.mid(x[0]))
		midPT = lastPT.mid2(x[0],-0.1)
		svgMID = svgMID + pathQTO(midPT,x[0])
		#svgMID = svgMID + pathLINETO(x[0])
		svgMID = svgMID + pathLINETO(x[1])
		svgMID = svgMID + pathARCTO(x[2],r=roller_radius,thing="0 0 0")
		svgMID = svgMID + pathLINETO(x[3])
		lastPT = x[3]

	svgMID = svgMID + endPATH(fill="#000")

	print('start')
	
	for t in midRAY:
		svgMID = svgMID + makeCIRCLE(t,r=2.0,fill="#f00",fillo="1.0",kolor="#f00",width="0",comment="cutout")
		middy = makeCIRCLE(t,r=20.0,fill="#f00",fillo="1.0",kolor="#f00",width="0",comment="cutout")
		print(t)
		print(type(middy))
        
	svgMID = svgMID + makeCIRCLE(D2(),r=leng-roller_radius+0.2,fill="#f00",fillo="1.0",kolor="#f00",width="0",comment="cutout")

	print(svgMID)

	ff = open('teeth2.svg','w')
	ff.write(makeSVG(svgMID))
	ff.close()

	#return midRAY, full_array


makeSPROCKET(15)

#cairosvg.svg2png(bytestring=makeSVG(svgMID),write_to='teeth.png')


