# Task 8

from cubic_generator import CubicGenerator

# Example usage of the CubicGenerator class
generator = CubicGenerator()
start = 1
end = 10

try:
    cubes = generator.generate_cubes(start, end)
    print("List of cubes from", start, "to", end, ":", cubes)
except ValueError as e:
    print("Error:", e)
