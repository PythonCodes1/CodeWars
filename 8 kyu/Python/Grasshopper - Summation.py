# Finding the factorial of a specified number
# 8 kyu

def summation(num):
    numb = 0
    numbs = 0  
    for i in range(0, num):
        numb = numb + (numbs + 1)
        numbs += 1
    return numb
