import svgwrite
import math
from D2stuff import *

# Create a D2 point
point1 = D2(10,120)
point2 = point1.vector_to(260,-20)

direction1 = point1.angle_to(point2)
point3 = point1.vector_to(1,direction1)

direction1 = point2.angle_to(point1)
point4 = point2.vector_to(1,direction1)

# Create an SVG drawing
dwg = svgwrite.Drawing('example.svg', profile='full')

# Create a circle at the D2 point

line1 = dwg.line(start=point1.xy(), end=point2.xy(), stroke_width=10, stroke='#357')
line2 = dwg.line(start=point3.xy(), end=point4.xy(), stroke_width=2, stroke='#fefefe')

# Add the circle to the SVG drawing
dwg.add(line1)
dwg.add(line2)

# Save the SVG file
dwg.save()
