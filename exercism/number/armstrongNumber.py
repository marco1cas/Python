def is_armstrong_number(number):
    s = str(number)
    dig = len(s)
    form = sum(int(d) ** dig for d in s)
    return form == number

#Second Version
def is_armstrong_number2(number):
    return number = sum(int(var) ** len(str(number)) for var in str(number))
    
