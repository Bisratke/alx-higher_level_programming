#!/usr/bin/python3
# 1-element_at.py


def element_at(my_list, idx):
    """Retrive an element from a list."""
    x = (len(my_list) - 1)
    if idx < 0 or idx > x:
        return None
    return (my_list[idx])
