#!/usr/bin/python3
import sys
def print_args():
    """Prints the number of and the list of its argumets."""

    num_args = len(sys.argv)
    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} arguments:")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i - 1]}")

if __name__ == "__main__":
    print_args()
