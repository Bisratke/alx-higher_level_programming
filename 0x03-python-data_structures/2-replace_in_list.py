#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    x = len(my_list)
    if idx >= 0 and idx < x:
        my_list[idx] = element
    return (my_list)
