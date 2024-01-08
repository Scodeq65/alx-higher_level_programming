#!/usr/bin/python3
for first_combo in range(10):
    for second_combo in range(first_combo + 1, 10):
        print("{:d}{:d}".format(first_combo, second_combo), end=', ' if first_combo < 8 or second_combo < 9 else "\n")
