"""This module contains code related to string manipulation
"""

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)


if __name__ == '__main__':
    forbidden = input('enter forbidden letters: ')
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count = count + 1
    print('number of words without forbidden letters: ', count)            
    fin.close()


