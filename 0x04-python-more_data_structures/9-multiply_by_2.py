#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = {}

    # Iterate ovr the key/value pairs in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and store it in the new dictionary
        multiplied_dict[key] = value * 2

    return (multiplied_dict)
