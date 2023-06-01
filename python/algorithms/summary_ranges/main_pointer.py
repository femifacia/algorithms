#!/usr/bin/env python3

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        if nums == []:
            return []
        a = nums[0]
        i=0
        size = len(nums)
        while i < size:
            left = i
            while i+1 < size and nums[i+1] == a+1:
                i+=1
                a+=1
            right = i
            tmp = str(nums[left]) + "->" + str(nums[right]) if left != i else str(nums[i])
            ans.append(tmp)
            if i + 1 < size:
                a = nums[i+1]
            i+=1
        return ans

                

