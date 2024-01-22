
from math import cos,sin,radians

def dcos(ang):
	return cos(radians(ang))
def dsin(ang):
	return sin(radians(ang))

output = '' 
output = output + '<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">\n'
output = output + '<rect width="100" height="100" fill="#fff" />\n'
output = output + '<circle cx="50" cy="50" r="29.5" transform="translate({xx},{yy})" fill="#444" />'
output = output + '<circle cx="50" cy="50" r="20" transform="translate({xx},{yy})" fill="#fff" />'


cradius = 30.54181308912523
gradius = cradius - 3.6
dradius = 7.9375 / 2.0

for t in range(15):
#
	cang = t * 24 + 12
	xx = dcos(cang) * gradius + 50 
	yy = dsin(cang) * -gradius + 50 
	output = output + f'<circle cx="0" cy="0" r="{dradius-0.5}" transform="translate({xx},{yy})" fill="#0aa" /> \n'
#
	cang = t * 24
	xx = dcos(cang) * cradius + 50
	yy = dsin(cang) * -cradius + 50
	output = output + f'<circle cx="0" cy="0" r="{dradius}" transform="translate({xx},{yy}) scale(1,1.3)" fill="#f00" /> \n'


output = output + '</svg>\n'

with open("sprocket.svg","w") as file:
	file.write(output)

