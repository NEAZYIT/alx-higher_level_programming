#!/usr/bin/python3
"""
Finds the peak value in a list of integers using binary search algorithm.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    for i in range(length - 1):
        if list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
    return list_of_integers[length - 1]
