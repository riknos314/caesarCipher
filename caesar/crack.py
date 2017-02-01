from caesar import shift

def findKey(aStr, dictionary):
    aStr = aStr.lower()
    testStr = aStr[:20]

    for j in range(len(testStr),2,-1):

        for i in range(26):
            possPlaintext = shift.shiftByNum(testStr, i)
            
            if possPlaintext[:j] in dictionary:
                return i
