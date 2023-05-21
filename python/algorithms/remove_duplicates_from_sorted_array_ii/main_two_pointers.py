#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = right = 0
        size = len(nums)

        while (right < size):
            nums[left] = nums[right]
            right +=1
            if (right < size and nums[right] == nums[left]):
                left += 1
                nums[left] = nums[right]
                while (right < size and nums[right] == nums[left]):
                    right +=1
            left += 1
        return left