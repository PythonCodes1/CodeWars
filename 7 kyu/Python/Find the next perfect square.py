# Returning the next perfect square if the input integer is a square. If not, return -1
# 7 kyu

import math

def find_next_square(sq):
    if (math.sqrt(sq)).is_integer():
         return int(math.sqrt(sq) + 1) **  2
    else:
        return-1
