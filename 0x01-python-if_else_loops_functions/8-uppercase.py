#!/usr/bin/python3
def uppercase(str):
    for i in str:
        code = ord(i)
        print("%c" % (code-32 if code in range(97, 123) else code), end="")
    print("")
