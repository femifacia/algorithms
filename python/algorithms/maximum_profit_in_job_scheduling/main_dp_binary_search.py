#!/usr/bin/env python

from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # We will sort intervals by start and end
        # we will create a dp array in which dp[i] is the highest value we can have 
        # from intervals starting at i and which don't overloop themselves
        ans = float('-inf')
        # We will create sorted arrays for intervals from start and end
        start_sort = sorted(startTime)
        end_sort = sorted(endTime)
        # we init the dp array
        dp = [0] * (len(start_sort) + 1)
        start_link = defaultdict(list)
        start_profit = defaultdict(list)
        # we will link every sorted start to its original and and very start with its 
        # profit
        for i in range(len(startTime)):
            start_link[startTime[i]].append(endTime[i])
            start_profit[startTime[i]].append(profit[i])
        # right is the rightest end of intervals seen
        right = end_sort[-1]
        for i in range(len(startTime) - 1, -1, -1):
            dp[i] = dp[i + 1]
            # if we see an interval which end by an already seen value, we skip it
            # and assign the previous value to the actual dp[i]
            if i + 1 < len(startTime) and end_sort[i] == end_sort[i + 1]:
                dp[i] = dp[i + 1]
                right = end_sort[i]
                continue
            # we find the left most starting position which start before 
            # the actual ending position
            left = bisect_left(start_sort,end_sort[i])
            
            # if this position is at the end of the array, we can skip this value
            if left >= len(startTime):
                right = end_sort[i]
                continue
            # Since we find a left, we will do a check for each intervals from left to
            # right
            while left < len(start_sort) and start_sort[left] < right:
                elm = start_sort[left]
                for x,y in zip(start_link[elm], start_profit[elm]):
                    # for each elm we calculate in tmp the value of its profit
                    # + the value of the highest possible value starting at the end
                    # of this interval
                    tmp = y + dp[bisect_left(end_sort, x)]
                    # dp[i] is so the max between this tmp, and dp[i]
                    dp [i] = max(dp[i], tmp)
                left += 1
            # we put right at end_sort[i]
            right = end_sort[i]
        left = 0
        # we will do the same as the previous loop but as start left = 0
        # to fill the remains dp positions with the startings remaining intervals
        while left < len(start_sort) and start_sort[left] < right:
            elm = start_sort[left]
            for x,y in zip(start_link[elm], start_profit[elm]):
                tmp = y + dp[bisect_left(end_sort, x)]
                ans = max(ans, tmp)
            left += 1
        dp_max = max(dp)
        # we return the max of dp
        return max(dp_max, ans)
sol = Solution()
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
print(sol.jobScheduling(startTime, endTime, profit))