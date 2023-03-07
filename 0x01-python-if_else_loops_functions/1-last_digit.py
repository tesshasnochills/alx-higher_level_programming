#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(f"Last digit of {number}", end=" ")

if number > 0:
    last = number % 10
else:
    number = number * -1
    last = number % 10

print(f"is {last}", end=" ")

if last > 5:
    print(f"and is greater than 5")
elif last == 0:
    print(f"and is zero")
else:
    print(f"and is less than 6 and not 0")

