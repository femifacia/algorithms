#!/usr/bin/env python3

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        arr1 = []
        arr2 = []
        for i in range(len(s)):
            #we map each val to an int
            #at the end we check if the two arr of ints are equals
            if not s[i] in dic1:
                dic1[s[i]] = i
            arr1.append(dic1[s[i]])
            if not t[i] in dic2:
                dic2[t[i]] = i
            arr2.append(dic2[t[i]])
        return (arr1 == arr2)

sol = Solution()
s1 = "abab"
s2 = "abcd"
print(sol.isIsomorphic(s1,s2))
