#!/usr/bin/env python3

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
        i = 0
        j = 0
        seen = set()
        size = len(nums)
        while (j < size and j < k):
            if nums[j] in seen:
                return True
            seen.add(nums[j])
            j+=1
        while j < size:
            if nums[j] in seen:
                return True
            seen.remove(nums[i])
            seen.add(nums[j])
            i+=1
            j+=1
        return False

sol = Solution()

nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums, k))