import math
from sys import argv

def calculate_deflection(length, outer_diameter, wall_thickness, load):
	inner_diameter = outer_diameter - 2 * wall_thickness
	moment_of_inertia = math.pi * (outer_diameter**4 - inner_diameter**4) / 32
	modulus_of_elasticity_steel = 200000
	load_N = load * 9.81
	deflection = (load_N * length**3) / (48 * modulus_of_elasticity_steel * moment_of_inertia)
	return deflection

def calculate_tube_weight(length, outer_diameter, wall_thickness):
	inner_diameter = outer_diameter - 2 * wall_thickness
	outer_volume = math.pi * (outer_diameter**2) / 4 * length
	inner_volume = math.pi * (inner_diameter**2) / 4 * length
	material_volume = outer_volume - inner_volume
	density_steel = 0.00000785
	weight = material_volume * density_steel
	return weight

length = float(argv[1])
outer_diameter = float(argv[2])
wall_thickness = float(argv[3])
load = float(argv[4])

deflection = calculate_deflection(length, outer_diameter, wall_thickness, load)
weight = calculate_tube_weight(length, outer_diameter, wall_thickness) * 1000

print(f"D: {deflection:.2f}mm / W: {weight:.0f}g")
