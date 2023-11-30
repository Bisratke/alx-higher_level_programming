#!/usr/bin/python3
if __name__ == "__main__":
    import sys
number_of_arguments = len(sys.argv)
if number_of_arguments == 1:
    print("0 arguments.")
else:
     print("{:d} argument".format(number_of_arguments  - 1), end="")
     if number_of_arguments  > 2:
            print("s", end="")
     print(":")
     for i in range(1, number_of_arguments ):
         print("{:d}: {:s}".format(i, sys.argv[i]))
