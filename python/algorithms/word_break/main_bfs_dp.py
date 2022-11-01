#!/usr/bin/env python3

from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        size = len(s)
        seen = {}
        dp = [""] * size
        sliding_window = ""
        i = 0
        to_see = deque()
        while (i < size and sliding_window != s and dp[-1] == ""):
            #print(s, i)
            sliding_window += s[i]
            if (sliding_window in wordDict):
                dp[i] = sliding_window
                if (not (sliding_window, i) in seen):
                    to_see.appendleft((sliding_window, i))
                    seen[(sliding_window, i)] = 1
                sliding_window = ""
            if i + 1 == size and to_see:
                sliding_window,i = to_see.pop()
            i += 1
        if (dp[-1]):
            return True
        return False

sol =Solution()
s = "leetcode"
wordDict = ["leet","code"]
s = "applepenapple"
wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
s = "femiestfrais"
wordDict = ["femi", "fem", "ie", "stfraiss"]
s = "aaaaaaaaaaaaaaaaaaaaaac"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(sol.wordBreak(s, wordDict))