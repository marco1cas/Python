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
