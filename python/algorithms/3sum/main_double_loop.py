#!/usr/bin/env python3

from collections import Counter

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        seen = Counter(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                tmp_sum = nums[i] + nums[j]
                if -tmp_sum in seen:
                    tmp = tuple(sorted((nums[i], nums[j], -tmp_sum)))
                    if -tmp_sum != nums[i] and -tmp_sum != nums[j]:
                        ans.add(tmp)
                    elif seen[-tmp_sum] >= 2 and nums[i] != nums[j]:
                        ans.add(tmp)
                    elif seen[-tmp_sum] >= 3:
                        ans.add(tmp)
        ans = [list(i) for  i in ans]
        return ans

sol = Solution()
nums = [-1,0,1,0]
print(sol.threeSum(nums))