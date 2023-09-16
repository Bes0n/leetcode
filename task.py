#!/usr/bin/python3.10

import itertools

class Solution:
    def maxRepeating(self, s: str) -> str:
        string = list(s)
        stack = []

        for curr in string:
            if stack:
                curr.isupper() 
        return "".join(stack)

# s = "leEeetcode"
s = "Pp"
# s = "s"

print(Solution.maxRepeating(Solution, s))