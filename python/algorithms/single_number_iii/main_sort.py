#!/usr/bin/env python3

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        size = len(nums)
        count = 0
        ans = []
#        print(nums)
        while (j < size and count != 2):
            if nums[i] != nums[j]:
                ans.append(nums[i])
                i+=1
                j+=1
                count += 1
                continue
            i+=2
            j+=2
        if nums[-1] != nums[-2]:
            ans.append(nums[-1])
        return ans

sol = Solution()
nums =  [1,2,1,3,2,5]
nums = [-1,0]
print(sol.singleNumber(nums))
