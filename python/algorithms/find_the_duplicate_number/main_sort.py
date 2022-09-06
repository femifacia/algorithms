#!/usr/bin/env python3

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        #by sorting the numbers the dupplicate number is obviously following itself
        #i used the sorted function cause the topic say to us to not modify the nums array
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i-1] == sorted_nums[i]:
                return (sorted_nums[i])
        return (-1)