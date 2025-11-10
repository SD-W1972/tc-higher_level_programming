#!/usr/bin/python3
from calculator_1 import add, sub, mul,div
import sys

if __name__ != "__main__":
    sys.exit(0)

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

import sys

a = int(sys.argv[1])
b = int(sys.argv[3])


if sys.argv[2] == "+":
    print("{} + {} = {}".format(a, b, (a+b)))
elif sys.argv[2] == "-":
    print("{} - {} = {}".format(a, b, (a-b)))
elif sys.argv[2] == "*":
    print("{} * {} = {}".format(a, b, (a*b)))
elif sys.argv[2] == "/":
    print("{} / {} = {}".format(a, b, (a/b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
    
