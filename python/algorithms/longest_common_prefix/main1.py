#!/usr/bin/env python3

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        size = len(strs)
        min_size = min(len(i) for i in strs)
        pref = ""
        for i in range(min_size):
            j = 1
            while (j < size and strs[j][i] == strs[j-1][i]):
                j+=1
            if j == size:
                pref += strs[j-1][i]
            else:
                return(pref)
        return pref

sol = Solution()
strs = ["afliwer","fli","fli"]
print(sol.longestCommonPrefix(strs))