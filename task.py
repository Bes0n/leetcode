#!/usr/bin/python3.10


s = ["h","e","l","l","o"]

left = 0
right = len(s) - 1

while left < right:
    x = s[right]
    y = s[left]
    s[right] = y
    s[left] = x
    left += 1
    right -= 1

print(s)

    