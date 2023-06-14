#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    # Update the value if the key exists in the dictionary
    if key in a_dictionary:
        a_dictionary[key] = value

    else:
        a_dictionary[key] = value

    return (a_dictionary)
