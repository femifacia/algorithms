#!/usr/bin/env python

class Solution:
    
    def dfs(self, s : str, i : int, parent) -> int:
        # We will use 3 variables to replace the use of the dp array
        # dp_0 is the dp[i + 0], the number of words that can be done
        # starting from pos i
        # 
        # dp_1 is the dp[1], the number of words that can be done starting from 
        # pos i + 1
        # 
        # dp_2 is the dp[i + 2], the number of words that can be done starting
        # from pos i + 2
        #  
        if i == self.size:
            # if the last character call dfs we can return as dp_0 1
            return 1,0,0
        if s[i] == "0":
            # if we find a 0, we will return as its dp_0, 0 but we will calculate
            # its dp_1 and dp_2
            if parent == 0:
                # parent is used to check if the parents was a 0 or not
                # if it is, we return 0,0,0 because it is not needed to continue
                return 0,0,0
            res = self.dfs(s, i+1, 0)
            # indeed if we are in a 0 case, dp_0 = 0 but we return the possibilities
            # after this 0
            return 0,res[0],res[1]
        res = self.dfs(s, i + 1, 1)
        dp_0 = 0
        dp_1 = res[0]
        dp_2 = 0
        # if we are in a position we can combine the actual number and the following
        # we will add the possibility of the second to our sum
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            dp_2  = res[1]
        dp_0 = dp_1 + dp_2
        return dp_0, dp_1, dp_2

    def numDecodings(self, s: str) -> int:
        self.size = len(s)
        dp_0, dp_1, dp_2 = self.dfs(s,0,1)
        return dp_0
    
sol = Solution()

s = "111111111111111111111111111111111111111111111"
s = "2611055971756562"
s='11200100234'
s = "111111111111111111111111111111111111111111111"
s = "2111"
print(sol.numDecodings(s))