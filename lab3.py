# Task 5
class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares


generator = SquareGenerator()
start = 10
end = 1

try:
    squares = generator.generate_squares(start, end)
    print("List of squares from", start, "to", end, ":", squares)
except ValueError as e:
    print("Error:", e)
