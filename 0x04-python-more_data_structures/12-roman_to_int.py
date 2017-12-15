#!/usr/bin/python3

def roman_to_int(roman_string):
    coins = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in roman_string:
        if i in roman:
            coins += roman[i]

    for _ in range(roman_string.count("IX") + roman_string.count("IV")):
        coins -= 2

    for _ in range(roman_string.count("XL") + roman_string.count("XC")):
        coins -= 20

    for _ in range(roman_string.count("CD") + roman_string.count("CM")):
        coins -= 200

    return (coins)
