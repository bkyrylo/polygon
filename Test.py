#!/usr/bin/env python3
"""
Test.py: Description of what HelloW does.
"""
# no import
__author__ = 'kyrylo'


def do_smth(a, default):
    if default is None:
        print("None")
    else:
        print("not None")

do_smth(5,
        None)
