# Task 2

def generate_squares(start, end):

    squares = [x**2 for x in range(start, end + 1)]
    return squares

start = 1
end = 10
result = generate_squares(start, end)
print("List of squares from", start, "to", end, ":", result)
