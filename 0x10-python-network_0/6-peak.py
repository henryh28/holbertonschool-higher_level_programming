#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds a peak in 'list_of_integers' """
    backup_peak = None

    for counter, value in enumerate(list_of_integers):
        if len(list_of_integers) < 2:  # list of 1
            return (value)

        if counter == 0:
            if value > list_of_integers[counter + 1]:
                backup_peak = value

        if counter != 0:
            if counter != len(list_of_integers) - 1:
                if value > list_of_integers[counter - 1] and \
                   value > list_of_integers[counter + 1]:
                    return (value)
            else:  # last element of list
                if backup_peak is not None:
                    return (backup_peak)
                else:
                    return (value if value > list_of_integers
                            [counter - 1] else None)
