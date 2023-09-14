#!/usr/bin/python3.10
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        if not stack:
            stack.append(s[0])
                            
        return "".join(stack)

s = "aababaab"

print(Solution.removeDuplicates(Solution,s))