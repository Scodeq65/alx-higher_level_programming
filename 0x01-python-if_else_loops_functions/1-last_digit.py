#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigits = abs(number) % 10
if number < 0:
    lastdigits = -(lastdigits)
dstring = "Last digit of {} is {}".format(number, lastdigits)
if lastdigits > 5:
    print(f"{dstring} and is greater than 5")
elif lastdigits == 0:
    print(f"{dstring} and is 0")
elif lastdigits < 6:
    print(f"{dstring} and is less than 6 and not 0")
