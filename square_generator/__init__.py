class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares
