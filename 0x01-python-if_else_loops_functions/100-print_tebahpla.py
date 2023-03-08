#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    letter = chr(c)
    if c % 2 == 0:
        letter = letter.upper()
    else:
        letter = letter.lower()
    print(letter, end="")

