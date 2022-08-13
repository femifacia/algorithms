#!/usr/bin/env python3

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1
        i = 0
        print(zero)
        print(one)
        print(two)
        while (zero):
            nums[i] = 0
            i+=1
            zero -= 1
        while (one):
            nums[i] = 1
            one -= 1
            i+=1
        while (two):
            nums[i] = 2
            i+=1
            two -= 1
sol = Solution()
arr = [2,0,2,1,1,0]
print(arr)
sol.sortColors(arr)
print(arr)