def steps(number):
    if number <= 0:
        return ValueError("Only positive integers are allowed")

    c = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        c += 1
    return c
