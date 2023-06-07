#!/usr/bin/env python3

import sys

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bin = list(map(int, bin(a)[2:]))
        b_bin = list(map(int, bin(b)[2:]))
        c_bin = list(map(int, bin(c)[2:]))
        ans = 0
        a_bin = ((32 - len(a_bin)) * [0]) + a_bin
        b_bin = ((32 - len(b_bin)) * [0]) + b_bin
        c_bin = ((32 - len(c_bin)) * [0]) + c_bin

#        print(a_bin,b_bin,c_bin,sep="\n")
        for i in range(31, -1, -1):
            if c_bin[i] == 0:
                if a_bin[i] == 1 and b_bin[i] == 1:
                    ans += 2
                elif a_bin[i] or b_bin[i]:
                    ans += 1
            else:
                if a_bin[i] or b_bin[i]:
                    continue
                ans += 1
        return ans


sol = Solution()
print(sol.minFlips(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))