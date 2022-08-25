#!/usr/bin/env python3

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if (s[i] in dic and dic[s[i]] != t[i]) or  (t[i] in dic.values() and dic.get(s[i], None) != t[i]):
                return (False)
            dic[s[i]] = t[i]
        return (True)

sol = Solution()
s1 = "foo"
s2 = "bar"
print(sol.isIsomorphic(s1,s2))
