#!/usr/bin/env python

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber < 27:
            return chr(64 + columnNumber)
        res = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            res = chr(65 + remainder) + res
        return res

import sys
sol = Solution()
print(sol.convertToTitle(int(sys.argv[1])))