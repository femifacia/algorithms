#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        print(nums,'ooo')
        size = len(nums)
        dp = [1] * size
        rank = defaultdict(int)
        lis = 1
        for i in range(len(nums) - 1, -1, -1):
            #rank[nums[i]] = 1
            print(i)
            for j in range(size -1, i, -1):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if not dp[i] in rank:
                        rank[dp[i]] = rank[dp[j]]
                    else:
                        rank[dp[j]] += 1
                    
            if dp[i] == 1:
                rank[1] +=1
            print("r",rank,nums[i],dp)
#                rank[dp[j] + 1] += 1
            #rank[dp[i]] += 1
        print(rank)
        print(dp)
        print("nums", nums)
        return rank[max(rank)]
    
sol = Solution()
nums = [1,2,4,3,5,4,7,2]
nums = [1,2,4,5]
nums = [2,2,2,2,2]
nums = [1,3,5,4,7]
print(sol.findNumberOfLIS(nums))