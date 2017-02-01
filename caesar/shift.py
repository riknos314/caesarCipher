import string


def shiftByNum(aStr, aNum):
    chrToIntlow = dict(zip(string.ascii_lowercase, range(26)))
    intToChrlow = dict(zip(range(26), string.ascii_lowercase))
    chrToIntHigh = dict(zip(string.ascii_uppercase, range(26,52)))
    intToChrHigh = dict(zip(range(26,52), string.ascii_uppercase))

    newStr = ''
    for c in aStr:
        if c in chrToIntlow: 
            newStr += intToChrlow[(chrToIntlow[c] + aNum) % 26]
        elif c in chrToIntHigh:
            newStr += intToChrHigh[(chrToIntHigh[c] + aNum) % 26 + 26]
        else:
            newStr += c

    return(newStr)

