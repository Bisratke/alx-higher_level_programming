
#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = magic_calculation_102.add(a, b)
    else:
        c = magic_calculation_102.sub(a, b)

    for i in range(4, 6):
        c = magic_calculation_102.add(c, i)

    return c
