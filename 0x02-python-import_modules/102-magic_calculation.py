#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    return (add(add(a, b), sum(add(a, b) for i in range(4, 6)))) if a < b else sub(a, b)
