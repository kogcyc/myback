from math import *
from D2 import *
a = 0.3
b = 1 - a
c = 360.0 / 5
d = c * a
e = c * b
f = 0
stroke_width = 2
radius = 50
fp = open('cutout.svg','w')
for t in range(5):
	f = f + d
	p = D2().vector(radius,f)
	f = f + e
	p2 = D2().vector(radius,f)
	out = f'<path d="M{round(p.x,1)},{round(p.y,1)} A {radius} {radius} 1 0 1 {round(p2.x,1)},{round(p2.y,1)}"  style="fill:#000;fill-opacity:0.0;stroke:#f00;stroke-width:{stroke_width};stroke-linecap:round" /> '
	fp.write(out)
fp.close()


