def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-", "")
    return len(string) == len(set(string))

#Second Version
def is_isogram2(string):
    letters = [i for i in string.lower() if i.isalpha()]
    return len(letters) == len(set(letters))
