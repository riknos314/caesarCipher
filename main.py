import dictionary
from caesar import crack
from caesar import shift

DICT = dictionary.engDict()

def crackSimple():
    f = open('cipher_in_simple.txt')

    word = f.readline()
    word = word.replace(u'\ufeff','')

    decryptKey = crack.findKey(word,DICT)
    newStr = ''
    
    newStr += shift.shiftByNum(word, decryptKey)

    for line in f:
        newStr += shift.shiftByNum(line, decryptKey)

    f.close()

    newFile = open('plaintext_out_simple.txt','w')

    newFile.write(newStr)

    return


def crackComplex():

    f = open('cipher_in.txt')

    contents = f.read()
    contents = contents.replace(u'\ufeff','')

    decryptKey = crack.findKey(contents,DICT)
    newStr = ''
    
    newStr += shift.shiftByNum(contents, decryptKey)


    f.close()

    newFile = open('plaintext_out.txt','w')

    newFile.write(newStr)

    return


def main():
    #crackSimple()
    #crackComplex()
    print(shift.shiftByNum('Mci aors wh hvwg tof. Qcbufohg!',12))


if __name__ == '__main__':
    main()
