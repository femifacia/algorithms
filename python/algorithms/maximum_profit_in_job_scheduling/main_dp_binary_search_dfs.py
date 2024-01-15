#!/usr/bin/env python

from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # We sort intervals by their startTime
        intervals = sorted(zip(startTime, endTime, profit))
        # We will use a cache such as cache[i] is the maximum profit we can have
        # for sorted intervals starting at i
        cache = {}
        def dfs(i):
            # if we outside the last intervam we return 0
            if i >= len(intervals):
                return 0
            # if the value is requested by an interval, instead of doing
            # the computation again we will just return its value saved in the cache
            if i in cache:
                return cache[i]
            # for each interval we will have to do a choice: include this interval and
            # the highest profit starting by the end of this interval or the next interval
            
            # indeed  we will say that cache[i] = cache[i+1] in the case where
            # cache[i + 1] > intervals[i][2] + cache[intervals[i][1]]
            
            # think about it or represent a scheme to help you visualizing
            
            # here res will contain the highest profit starting from i + 1
            res = dfs(i + 1)
            
            # now we have to calculate intervals[i][2] + cache[intervals[i][1]]
            
            # we first need to know where is the position of this interval in the
            # sorted array
            
            # we will use bisection to do so
            
            # previously I used parameters such as lo = i, key = lambda x : x[0]
            # I tried the following parameters after see it on a forum and this works to
            #j = bisect_left(intervals,intervals[i][1],i,key= lambda x: x[0])
            j = bisect_left(intervals,(intervals[i][1],-1,-1))
            
            # then we compare our to values and assign the highest to cache[i]
            res = max(res, dfs(j) + intervals[i][2])
            cache[i] = res
            return res
#        dfs(0)
        return dfs(0)
sol = Solution()
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

startTime = [2,1,1]
endTime = [5,2,4]
profit = [5,6,4]
print("ok",sol.jobScheduling(startTime, endTime, profit))