#!/usr/bin/python3.10
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []

        for c in s:
            if c != '' and c != '.' and c != '..':
                stack.append(c)
            elif c == '..' and stack:
                stack.pop()
        
        return "/" + "/".join(stack)
    
# path = "/a/./b/../../c/"
# path = "//home//foo//"
# path = "/home//../"
path = "/../"

print(Solution.simplifyPath(Solution,path))
