"""This module contains code related to Caesar Cipher
"""

def rotate_letter(letter, n):
    """Rotates a letter by n places.

    letter: single character
    n: integer

    Returns: character
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    code = ord(letter) - start
    i = (code + n) % 26 + start
    return chr(i)
    
def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    new_word = ''
    for letter in word:
        new_word += rotate_letter(letter, n)
    return new_word

if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
    

        
        
        
        
