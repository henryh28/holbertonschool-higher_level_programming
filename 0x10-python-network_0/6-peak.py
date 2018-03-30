#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds a peak in 'list_of_integers' """

    if list_of_integers:
        peak = list_of_integers[0]

        for counter, value in enumerate(list_of_integers):
            if counter != len(list_of_integers) - 1:
                if value > list_of_integers[counter + 1]:
                    return (value)
            else:
                if value > list_of_integers[counter - 1]:
                    return (value)

        return (peak)
