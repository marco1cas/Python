def is_pangram(sentence):
    a = "abcdefghyjkmnopqrstuvwxyz"
    for i in a:
        if i not in sentence.lower():
            return False
    return True
