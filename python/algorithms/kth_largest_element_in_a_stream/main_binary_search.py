#!/usr/bin/env python3

from bisect import bisect_left

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        k = bisect_left(self.nums, val)
        self.nums.insert(k,val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)