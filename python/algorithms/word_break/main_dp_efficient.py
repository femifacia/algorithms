#!/usr/bin/env python3

from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i  +len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if (dp[i]):
                    break
        return dp[0]

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