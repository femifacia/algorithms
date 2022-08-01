#!/usr/bin/env python3


import sys

class Solution:
    def isValid(self, s: str) -> bool:
        correspondance = {'}' : '{', ')' : '(', ']' : '['}
        size = 0
        stack = []
        for i in s:
            if i not in correspondance:
                size += 1
                stack.append(i)
            else:
                if (size > 0):
                    elm = stack.pop()
                    if elm != correspondance[i]:
                        return (False)
                    size -= 1
                else:
                    return (False)
        if (size > 0):
            return (False)
        return (True)

sol = Solution()
print(sol.isValid(sys.argv[1]))