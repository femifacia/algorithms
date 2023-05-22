#!/usr/bin/env python3

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # b[k] will contain for index k the last element of the longest subsequence of size k
        n = len(nums)
        b = [float('-inf')]
        #b_index[k] == the index of nums when we have the longest subsequence of size k
        b_index = [None]
        #this array contain the index of the predecessor of each element
        predecessors = [None] * n
        for i in range(n):
            if nums[i] > b[-1]:
                b.append(nums[i])
                b_index.append(i)
                predecessors[i] = b_index[-1]
            else:
                k = bisect_left(b, nums[i])
                b[k] = nums[i]
                b_index[k] = i
                predecessors[i] = b_index[k-1]
        return len(b) - 1


nums = [10,9,2,5,3,7,101,18,1,2,3,4,5,6,7]
sol = Solution()
print(sol.lengthOfLIS(nums))