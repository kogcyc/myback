from D2stuff import *

circle = DCircle(center=D2(2.0, 3.0), radius=5.0)
line = D2line(m=2.0, b=D2(0.0, 1.0), xi=D2(1.0, 0.0))
intersections = circle.intersection_points(line)
for point in intersections:
    print(f"Intersection point: {point}")