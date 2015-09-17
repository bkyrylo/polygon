#!/usr/bin/env python3
"""
HelloW.py: Description of what HelloW does.
"""
import sys
import Module1
__author__ = 'kyrylo'

print(sys.argv[1])

print("Hello", "World!")

total = 0
count = 0

while True:
    try:
        line = input("integer: ")
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("count = ", count, "total = ", total, "mean = ", total / count)

#Module1.get_int("Hi: ")



