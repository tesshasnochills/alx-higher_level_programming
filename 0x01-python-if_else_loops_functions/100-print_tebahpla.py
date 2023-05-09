#!/usr/bin/python3

alphabet = ""
for x in reversed(range(97, 123)):
    if x % 2 == 0:
        alphabet = chr(x)
    else:
        alphabet = chr(x - 32)
    print("{}".format(alphabet), end="")
