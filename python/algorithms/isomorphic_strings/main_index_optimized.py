#!/usr/bin/env python3

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            #we map each val to the same int
            #if at any time the mapped values are different we stop.
            #it is the same principle with main_index but this time we don't append values
            #we do the check each turn
            if not s[i] in dic1:
                dic1[s[i]] = i
            if not t[i] in dic2:
                dic2[t[i]] = i
            if dic2[t[i]] != dic1[s[i]]:
                return False
        return (True)

sol = Solution()
s1 = "abab"
s2 = "abcd"
print(sol.isIsomorphic(s1,s2))
