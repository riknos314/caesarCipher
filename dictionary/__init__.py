#! python3

def engDict():
    f = open('wordlist_english.txt')

    words = set()

    for line in f:
        words.add(line.strip())

    f.close()

    return words

