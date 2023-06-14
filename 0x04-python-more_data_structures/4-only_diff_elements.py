#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = set()

    # Iterate over each element in set_1
    for i in set_1:
        # Check if the element is not present in set_2
        if i not in set_2:
            # Add the unique elemnt to the unique_elements set
            unique_elements.add(i)

    # Iterate over each element in  set_2
    for i in set_2:
        # Check i the element is not present in  set_1
        if i not in set_1:
            unique_elements.add(i)

    return (unique_elements)
