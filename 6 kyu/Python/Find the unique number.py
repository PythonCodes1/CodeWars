# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    arr.sort()
    # If length of index 0 is less than the length of index -1
    # And length of index 0 is less than the length of intex -2
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]


    return n
