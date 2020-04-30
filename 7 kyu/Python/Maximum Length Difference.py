"""
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

#Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13

https://www.codewars.com/kata/5663f5305102699bad000056/train/python
"""

def mxdiflg(a1,a2):
    allmax = []
    counter = 0
    if len(a1) and len(a2) != 0:
        if len(a1) > len(a2):
            while counter <=len(a1):
                for x in a1:
                    for y in a2:
                        allmax.append(abs(len(x)-len(y)))
                        counter+=1
            return max(allmax)
        if len(a1) <= len(a2) :
            while counter <=len(a2):
                for x in a1:
                    for y in a2:
                        allmax.append(abs(len(x)-len(y)))
                        counter+=1
            return max(allmax)
    if not a1 or not a2:
         return (-1)
