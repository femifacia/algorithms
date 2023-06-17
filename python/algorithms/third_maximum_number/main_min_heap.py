#!/usr/bin/env python3
import heapq

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap) > 3:
                heapq.heappop(heap)
        return heapq.heappop(heap)