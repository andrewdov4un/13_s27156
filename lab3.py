from cubic_generator import CubicGenerator

# Example usage of the CubicGenerator class
generator = CubicGenerator()
start = 1
end = 10

try:
    squares = generator.generate_squares(start, end)
    print("List of squares from", start, "to", end, ":", squares)
except ValueError as e:
    print("Error:", e)
