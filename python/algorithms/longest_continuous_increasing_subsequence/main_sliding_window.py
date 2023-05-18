#!/usr/bin/env python3

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        size = len(nums)
        right = 1
        left = 0
        longest_sequence_size = 1
        while (right < size):
            if (nums[right] <= nums[right-1]):
                longest_sequence_size = max(longest_sequence_size, right - left )
                if right + longest_sequence_size > size:
                    return longest_sequence_size
                left = right
            right += 1
        longest_sequence_size = max(longest_sequence_size, right - left)
        return longest_sequence_size

sol = Solution()
arr = [1,3,5,4,2,3,4,5]
print(sol.findLengthOfLCIS(arr))