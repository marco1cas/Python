def is_armstrong_number(number):
    s = str(number)
    dig = len(s)
    form = sum(int(d) ** dig for d in s)
    return form == number
