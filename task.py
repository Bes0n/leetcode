#!/usr/bin/python3.10

# arr = [1,1,3,3,5,5,7,7]
arr = [1,2,3]
# arr = [0,1]

def func(arr):
    n = set(arr)
    total = 0
    for x in arr:
        if x + 1 in n:
            total += 1
    return total

print(func(arr))