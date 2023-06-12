#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return (my_list) # Return the original list without any changes
    # Check if the list is None
    if my_list is None:
        return (None) # Return None if the list is None

    del my_list[idx] # Delete the item at the specified index
    return (my_list) # Return the modified list
