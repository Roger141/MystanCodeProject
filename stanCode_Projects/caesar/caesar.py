"""
File: caesar.py
Name:Roger141
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret = int(input('Secret number: '))
    ciphered = input("What's the ciphered string? ")
    ciphered = ciphered.upper()
    new_alphabet = shift_alphabet(secret)
    result = decipher(ciphered, new_alphabet)

    print('The deciphered string is:', result)


def shift_alphabet(n):
    """
    Deciphers a Caesar cipher string using a user-provided shift value.
    """
    n = n % 26
    return ALPHABET[-n:] + ALPHABET[:-n]

def decipher(cipher, new_alphabet):
    result = ''
    for ch in cipher:
        if ch.isalpha():
            idx = new_alphabet.index(ch)
            result += ALPHABET[idx]
        else:
            result += ch
    return result


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
