#!/usr/bin/env python3


class Solution:

    def qSelect(self, nums : list[int], p : int, start : int) -> int:
        i = p
        while (i < start):
            if nums[i] < nums[start]:
                nums[i], nums[p] = nums[p], nums[i]
                p+=1
            i+=1
        nums[p], nums[start] = nums[start], nums[p]
        return p

    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k
        start = 0
        end = len(nums) - 1
        while 1:
            p = self.qSelect(nums,start,end)
            if target < p:
                end = p - 1
            elif target > p :
                start = p + 1
            else:
                return nums[p]

sol = Solution()
nums = [5,4,3,2,1,10,11,58,-6]
k = 1
print(sol.findKthLargest(nums, k))
