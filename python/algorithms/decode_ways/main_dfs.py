#!/usr/bin/env python

class Solution:
    
    def dfs(self, s : str, i : int) -> int:
#        print(i)
# Try to decompose the problem with  a case with as s "2", "13", "213" or to look 
# at the notion
        if i in self.dic:
            return self.dic[i]
        if s[i] == "0":
            return 0
        res = self.dfs(s, i + 1)
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            res += self.dfs(s, i + 2)
        self.dic[i] = res
        return res

    def numDecodings(self, s: str) -> int:
        self.dic = {len(s) : 1}
        return self.dfs(s,0)
    
sol = Solution()

s = "111111111111111111111111111111111111111111111"
s = "111111111111111111111111111111111111111111111"
s = "2611055971756562"
s='11'
print(sol.numDecodings(s))