#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    kv = {"+": add, "-": sub, "*": mul, "/": div}

    for key in kv:
        if (key == argv[2]):
            print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, kv[key](a, b)))
            exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
