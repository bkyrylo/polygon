"""
Module1.py: Description of what Module1 does.
"""
# no imports
__author__ = 'kyrylo'

def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err1:
            print(err1)
