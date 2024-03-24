from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if start > end:
            raise ValueError("Start of range must be less than or equal to end")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares
