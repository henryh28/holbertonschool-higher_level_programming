#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not(i % 15):
            print("FizzBuzz", end=" ")
        elif not(i % 5):
            print("Buzz", end=" ")
        elif not(i % 3):
            print("Fizz", end=" ")
        else:
            print("%d" % (i), end=" ")


# Reference: print("FizzBuzz"[i * i%3 * 4:8 - (-i ** 4%5)] or i, end=" ")
