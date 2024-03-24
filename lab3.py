# Task 3

class SquareGenerator:
    def generate_squares(self, start, end):
        """
        Generate a list of squares for the range of numbers from start to end (inclusive).
        """
        squares = [x**2 for x in range(start, end + 1)]
        return squares

# Example usage of the SquareGenerator class
generator = SquareGenerator()
start = 1
end = 10
result = generator.generate_squares(start, end)
print("List of squares from", start, "to", end, ":", result)

