#!/usr/bin/env python3

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
        i = 0
        seen = {}
        size = len(nums)
        while i < size:
            if nums[i] in seen:
                if i-seen[nums[i]] <= k:
                    return True
            seen[nums[i]] = i
            i+=1
        return False


sol = Solution()

nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums, k))