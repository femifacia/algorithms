#!/usr/bin/env python3

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        size = len(nums)
        i = 1
        sequence_size = 1
        longest_sequence_size = 1
        while (i < size):
            if (nums[i] > nums[i-1]):
                sequence_size += 1
            else:
                longest_sequence_size = max(longest_sequence_size, sequence_size)
                sequence_size = 1
                if i + longest_sequence_size > size:
                    return longest_sequence_size
            i+=1
        longest_sequence_size = max(longest_sequence_size, sequence_size)
        return longest_sequence_size

sol = Solution()
arr = [1,3,5,4,2,3,4,5]
print(sol.findLengthOfLCIS(arr))