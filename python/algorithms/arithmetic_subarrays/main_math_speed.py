#!/usr/bin/env python

class Solution:
    
    def isArithmeticSequence(self, nums, left, right) -> bool:
        i = left
        max_tmp = float('-inf')
        min_tmp = float('inf')
        while i <= right:
            max_tmp = max(max_tmp, nums[i])
            min_tmp = min(min_tmp, nums[i])
            i+=1
        # the diff has to be divisible by the number of elements if we are
        # facing an arithmetic sequence
        if (max_tmp - min_tmp) % (right-left) != 0:
            return False
        step = (max_tmp - min_tmp) // (right-left)
        # array is constituate with same elemnt
        if not step:
            return True
        seen = set()
        i = left
        while i <= right:
            if nums[i] in seen:
                return False
            seen.add(nums[i])
            if (nums[i] - min_tmp) % step:
                return False
            i += 1
        return True
    
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ans = []
        mem = {}
        for a,b in zip(l,r):
            if (a,b) in mem:
                ans.append(mem[(a,b)])
                continue
            ans.append(self.isArithmeticSequence(nums,a,b))
            mem[(a,b)] = ans[-1]
        return ans