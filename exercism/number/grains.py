def square(number):
    if number < 1 or number > 64:
        return ValueError("Square must be between 1 and 64")
    return 2 ** (number - 1)
    
def total():
    return (2**64) - 1
    
#Second Version
SIXTY_FOUR = 64
def square2(number):
    if number not in  range(1, SIXTY_FOUR, +1):
        raise ValueError("Square must be between 1 and 64")
    return 2 ** (number - 1)

def total2():
    return (2** SIXTY_FOUR) - 1
