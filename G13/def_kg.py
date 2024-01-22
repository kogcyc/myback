import math

def calculate_deflection(length, outer_diameter, wall_thickness, load):
    # Convert dimensions to meters
    length /= 1000  # Convert mm to meters
    outer_diameter /= 1000
    wall_thickness /= 1000

    # Calculate inner diameter
    inner_diameter = outer_diameter - 2 * wall_thickness

    # Calculate moment of inertia
    moment_of_inertia = math.pi * (outer_diameter**4 - inner_diameter**4) / 32

    # Modulus of Elasticity for steel (in MPa)
    modulus_of_elasticity_steel = 200000

    # Calculate deflection using the formula
    deflection = (load * length**3) / (48 * modulus_of_elasticity_steel * moment_of_inertia)

    return deflection

# Example usage
length = float(input("Enter the length of the tube (mm): "))
outer_diameter = float(input("Enter the outer diameter of the tube (mm): "))
wall_thickness = float(input("Enter the wall thickness of the tube (mm): "))
load = float(input("Enter the applied load (N): "))

deflection = calculate_deflection(length, outer_diameter, wall_thickness, load)
print(f"The deflection of the tube is {deflection:.6f} meters.")





import math

def calculate_deflection(length, outer_diameter, wall_thickness, load_kg):
    # Convert dimensions to meters
    length /= 1000  # Convert mm to meters
    outer_diameter /= 1000
    wall_thickness /= 1000

    # Calculate inner diameter
    inner_diameter = outer_diameter - 2 * wall_thickness

    # Calculate moment of inertia
    moment_of_inertia = math.pi * (outer_diameter**4 - inner_diameter**4) / 32

    # Modulus of Elasticity for steel (in MPa)
    modulus_of_elasticity_steel = 200000

    # Convert load from kg to Newtons
    load_N = load_kg * 9.81

    # Calculate deflection using the formula
    deflection = (load_N * length**3) / (48 * modulus_of_elasticity_steel * moment_of_inertia)

    return deflection

# Example usage
length = float(input("Enter the length of the tube (mm): "))
outer_diameter = float(input("Enter the outer diameter of the tube (mm): "))
wall_thickness = float(input("Enter the wall thickness of the tube (mm): "))
load_kg = float(input("Enter the applied load (kg): "))

deflection = calculate_deflection(length, outer_diameter, wall_thickness, load_kg)
print(f"The deflection of the tube is {deflection:.6f} meters.")
