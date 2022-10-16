#!/usr/bin/env python3

class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            string = str(nums[i])
            nums.append(int(string[-1::-1]))
        nums.sort()
#        print(nums)
        size = len(nums)
        i = 0
        while i< size:
            count +=1
            c = nums[i]
#            print(c)
            if i + 1 < size and nums[i + 1] == c:
                while (i < size and nums[i] == c):
                    i+=1
            else:
                i += 1
        return count


sol = Solution()
nums = [89904,846787,965070,396570,847607,625317,851503,143414,954838,837423,988190,916423,771555,680073,575614,967207,965688]
nums = [1,13,10,12,31]
print(sol.countDistinctIntegers(nums))