# given an input STRING and number of chars to shift SHIFT_AMOUNT
# shift each alphabetic character left or right by SHIFT_AMOUNT
# if SHIFT_AMOUNT < 0, shift left
# if SHIFT_AMOUNT > 0, shift right
# return the resulting SHIFTEDSTRING
import string

def caesar_cipher(string, shift_amount):
    shiftedString = ""

    for ch in string:
        if (ch.isalpha()):
            if (ch.islower()):
                shiftedString += chr(((ord(ch) + shift_amount - ord('a')) % 26) + ord('a'))
            else: 
                shiftedString += chr(((ord(ch) + shift_amount - ord('A')) % 26) + ord('A'))
        else:
            shiftedString += ch
    
    return shiftedString

