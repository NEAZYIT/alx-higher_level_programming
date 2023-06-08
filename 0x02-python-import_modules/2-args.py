#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num_args = len(args)

    if num_args > 1:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))

    elif num_args == 0:
        print("{} arguments.".format(num_args))

    else:
        print("{} arguments:".format(num_args))
        print("{}: {}".format(num_args, args[0])
