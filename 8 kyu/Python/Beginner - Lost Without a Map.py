# Tried using lambda to solve this problem
# Doubles the integers in an array
# 8 kyu

def maps(a):
    result = map(lambda x: x + x, a) 
    return list(result)
