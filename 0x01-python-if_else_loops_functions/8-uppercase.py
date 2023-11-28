#!/usr/bin/python3


def uppercase(str):
    for t in str:
        e = ord(t)
        if e >= 97 and e <= 122:
            pr = chr(e - 32)
        else:
            pr = t
        print('{}'.format(pr), end="")
    print()
