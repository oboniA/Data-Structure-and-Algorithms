"""
Write a Python program to get a list,
sorted in increasing order
by the last count_item in each tuple
from a given list of
non-empty tuples.
"""

def last(n):
    return n[-1]

def sort(a):
    return sorted(a, key=last)