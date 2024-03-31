#!/usr/bin/env python

from bisect import bisect_left

from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        intervals = sorted(events, key = lambda x : x[0])
#        print(intervals)
        self.res = 0
        dp = {}
        def dfs(i):
            if i >= len(intervals):
                return 0
            if i in dp:
                return dp[i]
            res = dfs(i + 1)
            j = bisect_left(intervals, intervals[i][1], lo = i, key = lambda x : x[0] - 1)
#            print(res)
            dp[i] = max(intervals[i][2], res)
#            print("for i,j",i,j)
            self.res = max(intervals[i][2] + dfs(j), dp[i], self.res)
#            print("res",self.res)
#            print(dp)
            return dp[i]
        dfs(0)
#        print("jjj",res)
        return self.res