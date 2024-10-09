def convert(number):
    save = []
    if number % 3 == 0:
        save.append("Pling")
    if number % 5 == 0:
        save.append("Plang")
    if number % 7 == 0:
        save.append("Plong")
    if not save:
        return str(number)

    return "".join(save)

#Second Version
def convert2(number):
    save = ''

    if number % 3 == 0:
        save += 'pling'
    if number % 5 == 0:
        save += 'plang'
    if number % 7 == 0:
        save += 'plong'

    return save or f'{number}'

#Thrid Version
def convert3(number):
    result = (('pling' if number % 3 == 0 else '') + 
            ('plang' if number % 5 == 0 else '') +
            ('plong' if number % 7 == 0 else ''))
    
    return result or number



