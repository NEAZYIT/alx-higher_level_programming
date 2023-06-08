#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage : {} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = None
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
    sys.exit(0)
