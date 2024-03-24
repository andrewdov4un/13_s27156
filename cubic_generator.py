from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        """
        Generate a list of squares for the range of numbers from start to end (inclusive).
        If the start is greater than the end, raise a ValueError.
        """
        if start > end:
            raise ValueError("Start of range must be less than or equal to end")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares
