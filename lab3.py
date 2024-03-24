import math

# Task 4

class SquareGenerator:
    def generate_squares(self, start, end):

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(x) for x in numbers]
        return square_roots

generator = SquareGenerator()
start = 1
end = 10
squares = generator.generate_squares(start, end)
print("List of squares from", start, "to", end, ":", squares)

square_roots = generator.calculate_square_roots(squares)
print("Square roots of the generated squares:", square_roots)
