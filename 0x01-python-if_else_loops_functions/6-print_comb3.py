#!/usr/bin/python3
for first_combo in range(10):
    for second_combo in range(first_combo + 1, 10):
        if first_combo == 8 and second_combo == 9:
            print("{}{}".format(first_combo, second_combo))
        else:
            print("{}{}".format(first_combo, second_combo), end=', ')
