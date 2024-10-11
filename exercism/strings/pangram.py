def is_pangram(sentence):
    a = "abcdefghyjkmnopqrstuvwxyz"
    for i in a:
        if i not in sentence.lower():
            return False
    return True

#Second Version 
Import string

def is_panagram2(sentence):
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))
