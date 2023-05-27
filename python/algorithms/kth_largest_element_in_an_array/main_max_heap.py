#!/usr/bin/env python3

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # if we had a max heap, we could have just build the heap and then
        # pop k time
        # Because there is no max heap in the heapq module
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k-=1
        return -heapq.heappop(nums)