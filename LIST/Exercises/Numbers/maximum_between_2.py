"""
Given two numbers, write a Python code to find the Maximum of these two numbers.
"""

def find_max(a, b):
    if a > b:
        return f"{a} is the maximum number between {a} & {b}"
    elif a < b:
        return f"{b} is the maximum number  between {a} & {b}"
    else:
        return f" between {a} & {b} are Both equal"


print(find_max(3, 4))