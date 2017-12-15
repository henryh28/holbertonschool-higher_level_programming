#1/usr/bin/python3


def weight_average(my_list=[]):
    top = bottom = 0

    if (my_list is None or my_list == []):
        return 0

    for x, y in my_list:
        top += x * y
        bottom += y

    return (top/bottom)
