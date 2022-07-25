"""
Write a Python program to converting an integer to a string in any base.
in this case base 16
inserted input: n (integer)
given input: base16
"""


def int_to_string(n, base_16):
    string_convert = "0123456789ABCDEF"

    if n < base_16:                 # if integer less than 16
        return string_convert[n]    # gives the value present in the index of n in the string
    else:
        return int_to_string(n//base_16, base_16) + string_convert[n % base_16]


print(int_to_string(36, 16))