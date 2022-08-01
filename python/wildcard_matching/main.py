#!/usr/bin/env python3

import sys

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_size = len(p)
        s_size = len(s)
        s = "0" + s
        p = "0" + p
        arr = [[0] * (p_size + 1)  for i in range(s_size + 1)]
        #arr[0] = [1] * (p_size + 1)
        arr[0][0] = 1
        for i in range (1, p_size + 1):
            if (p[i] == '*'):
                arr[0][i] = arr[0][i - 1]
        for i in range (1, s_size + 1):
            for j in range (1, p_size + 1):
#                print(i, j, p)
                if (p[j] == '*'):
                    arr[i][j] = arr[i-1][j] or arr[i][j - 1]
                elif (p[j] == '?' or p[j] == s[i]):
                    arr[i][j] = (arr[i-1][j-1])
                else:
                    arr[i][j] = 0
        return arr[s_size][p_size]
sol = Solution()

print(sol.isMatch(sys.argv[1], sys.argv[2]))