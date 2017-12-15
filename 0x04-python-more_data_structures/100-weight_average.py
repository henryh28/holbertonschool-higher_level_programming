#1/usr/bin/python3


def weight_average(my_list=[]):
    top = bottom = 0

    if (my_list):
        for x, y in my_list:
            top += x * y
            bottom += y

    return (top/bottom if my_list else 0)
