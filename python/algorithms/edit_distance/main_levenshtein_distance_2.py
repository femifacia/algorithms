#!/usr/bin/env python3

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lev = [[i + j for i in range(len(word1) + 1 )] for j in range(len(word2) + 1)]

#        [print(i) for i in lev]

        word1 = "0" + word1
        word2 = "0" + word2
        for i in range(1, len(word2)):
            for j in range(1, len(word1)):
                lev[i][j] = min(lev[i -1][j] + 1, lev[i][j - 1] + 1, lev[i-1][j-1] + (1 if word1[j] != word2[i] else 0))
#        [print(i) for i in lev]
        return lev[-1][-1]

sol = Solution()
x = "sap"
y = "pac"
print(sol.minDistance(x,y))