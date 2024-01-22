from D2 import *

def rotateRAY(ray,angle):
	returnRAY = []
	for pt in ray:
		newPT = pt.rotzero(angle)
		returnRAY.append(newPT)
	return returnRAY
		

a = D2(3,3)
b = D2(4,-4)

rayray = [a,b]

rotated_ray = rotateRAY(rayray,-90)

for point in rotated_ray:
	print(f'{point.x} : {point.y}')


