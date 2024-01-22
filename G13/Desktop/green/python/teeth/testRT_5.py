
from sys import argv
from D2 import *
from svgLIBmm import *
#import cairosvg

def fakeHYP(l,c):
	a = float(l)*c
	b = a / 6.283185307179586 # 2 pi
	return b

def realHYP(l,c):
	a = 360.0/(c*2.0)
	h = (l/2.0) / sin(radians(a))
	return h

def makeSPROCKET(teeth):

	tooth_length = 12.0
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

	leng = fakeHYP(12.7,teeth)

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
		midPT = lastPT.mid2(x[0],17)
		svgMID = svgMID + pathQTO(midPT,x[0])
		#svgMID = svgMID + pathLINETO(x[0])
		svgMID = svgMID + pathLINETO(x[1])
		svgMID = svgMID + pathARCTO(x[2],r=roller_radius,thing="0 0 0")
		svgMID = svgMID + pathLINETO(x[3])
		lastPT = x[3]

	svgMID = svgMID + endPATH(fill="#000")

	for t in midRAY:
		svgMID = svgMID + makeCIRCLE(t,r=2.0,fill="#00",fillo="1.0",kolor="#f00",width="0",comment="")

	ff = open('teeth.svg','w')
	ff.write(makeSVG(svgMID))
	ff.close()

	#return midRAY, full_array


makeSPROCKET(34)

#cairosvg.svg2png(bytestring=makeSVG(svgMID),write_to='teeth.png')


