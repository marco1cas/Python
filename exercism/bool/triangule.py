def triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and (a + b >= c) and (b + c >= a) and (a + c >= b)


def equilateral(sides):
    if not triangle(sides):
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    if not triangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and a != c
