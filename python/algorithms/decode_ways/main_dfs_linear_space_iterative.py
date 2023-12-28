#!/usr/bin/env python

class Solution:

# look at the solution without variables recursive for explanations

    def numDecodings(self, s: str) -> int:
        size = len(s)
        dp_0, dp_1, dp_2 = 0,1 if s[-1] != "0" else 0,0
        i = size
        while i > 0:
            i-=1
            if s[i] == "0":
                dp_0 = 0
                dp_1, dp_2 = dp_0, dp_1
                continue
            dp_0 = dp_1
            if i + 1 < size and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp_0 += dp_2
            dp_1, dp_2 = dp_0, dp_1
        return dp_0
    
sol = Solution()

s = "111111111111111111111111111111111111111111111"
s = "2611055971756562"
s='11200100234'
s = "9919"
s="2111"
s = "111111111111111111111111111111111111111111111"
print(sol.numDecodings(s))