#!/usr/bin/env python3

#it works but it is to slow

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        return max(self.longestCommonSubsequence(text1[1:], text2), self.longestCommonSubsequence(text1, text2[1:]))

sol = Solution()
print(sol.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))