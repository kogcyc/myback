import math

def distance_to_polygon_corner(N, side_length):
    if N < 3:
        raise ValueError("A polygon must have at least 3 sides")
    
    # Calculate the distance to the corner using trigonometry
    distance = side_length / (2 * math.sin(math.pi / N))
    
    return distance

# Input parameters
N = int(input("Enter the number of sides of the regular polygon: "))
side_length = float(input("Enter the length of each side of the polygon: "))

# Calculate and print the distance to the corner
distance = distance_to_polygon_corner(N, side_length)
print(f"The distance from the origin to a corner of the {N}-sided polygon is: {distance}")
