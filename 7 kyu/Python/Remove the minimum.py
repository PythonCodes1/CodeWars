"""
Problem: 
Given an array of integers, remove the smallest value. 
Do not mutate the original array/list. If there are multiple
elements with the same value, remove the one with a lower index.
If you get an empty array/list, return an empty array/list.

Solution:
-Create a new copy of the list
-See if it's less than 1 (then return it)
-Remove the minimum of the copy

https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
"""

def remove_smallest(numbers):
    num = numbers.copy()
    if len(num) < 1 :
        return num
    else:
        num.remove(min(num))
        return num
