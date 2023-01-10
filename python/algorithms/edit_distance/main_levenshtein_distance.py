#!/usr/bin/env python3

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        A = [[i + j for j in range(m + 1)] for i in range(n + 1)]
        [print(i) for i in A]
#        print("ok")
        for i in range(n):
            for j in range(m):
                A[i + 1][j + 1] = min(A[i][j + 1] + 1, A[i + 1][j] + 1, A[i][j] + int(word1[i] != word2[j]))
        [print(i) for i in A]
        return A[n][m]

sol = Solution()
x = "sap"
y = "pac"
print(sol.minDistance(x,y))