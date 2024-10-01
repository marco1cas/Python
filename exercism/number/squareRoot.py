import math

def square_root(number):
    if number <= 0:
        raise ValueError("The radicand must be a positive natural number.")
    return math.isqrt(number)
