import math

def calculate_distance_to_vertex(n, a):
	angle = math.pi / n
	distance = a / math.tan(angle)
	return distance

# Example usage:
num_sides = 6  # Replace with the desired number of sides
apothem = 7.5  # Replace with the desired apothem length

result = calculate_distance_to_vertex(num_sides, apothem)
print(f"The distance from the center to a vertex is: {result}")

pth = ''
ang = 2*math.pi / num_sides
for t in range(num_sides):
	x = round(math.cos(ang*t)*result,2)
	y = round(math.sin(ang*t)*result,2)
	print(f'<circle cx="{x}" cy="{y}" r="{apothem*2}" fill="#ace"/>')