#!/usr/bin/python3
""" Class to JSON module """


def class_to_json(obj):
    """ Converts a class instance to a JSON representation """

    return (obj.__dict__)
