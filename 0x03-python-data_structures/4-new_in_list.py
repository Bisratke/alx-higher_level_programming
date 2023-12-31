#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    x = (len(my_list) - 1)
    if idx >= 0 and idx <= x:
        my_list[idx] = element
    return my_list
