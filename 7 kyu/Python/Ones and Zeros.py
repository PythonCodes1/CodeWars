"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
"""

def binary_array_to_number(arr):
    total = 0
    i = 1
    for num in arr[::-1]:
        total += (i*num)
        i *= 2
    return total
