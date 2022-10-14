#!/usr/bin/env python3

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if (not val in nums ):
            return len(nums)
        nbr = 0
        size = len(nums)
        nums.sort()
        idx = nums.index(val)
        while (idx < size and nums[idx] == val  and size -1 -nbr >= idx):
            nums[idx], nums[size -1 - nbr] = nums[size - 1 - nbr], nums[idx]
            idx, nbr = idx + 1, nbr + 1
        return size - nums.count(val)

sol = Solution()
nums = [2,3,2,3]
val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val))
print(nums)