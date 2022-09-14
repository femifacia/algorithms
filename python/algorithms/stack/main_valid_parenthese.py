#!/usr/bin/env python3

import sys


class Solution:
    def isValid(self, s: str) -> bool:
        correspondance = {')': '(', '}' : '{', ']': '['}
        st = []
        if (len(s) % 2):
            return (False)
        for i in range(len(s)):
            if not s[i] in correspondance:
                st.append(s[i])
                continue
            if (st and correspondance[s[i]] == st.pop()):
                continue
            else:
                return False
        if (st):
            return False
        return True

sol = Solution()
string = sys.argv[1]
print(string)
print(sol.isValid(string))