def is_paired(input_string):
    abierto = "[{("
    cerrado = "]})"
    arr = []
    for i in input_string:
        if i in abierto:
            arr.append(i)
        elif i in cerrado:
            if not arr or abierto[cerrado.index(i)] != arr.pop():
                return False
    return not arr

#Second Version
def is_paired2(input_string):
    abierto = "[{("
    cerrado = "]})"
    pairs = {')': '(', '}':'{', ']':'['}
    arr = []
    for i in input_string:
        if i in abierto:
            arr.append(i)
        elif i in cerrado:
            if not arr or arr.pop() != pairs[i]:
                return False
    return not arr
