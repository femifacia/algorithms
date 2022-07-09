#!/usr/bin/env python3

import sys

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_diff = {}
        for index, i in enumerate(nums):
            print(i, index, target)
            diff = target - i
            if (diff in map_diff.keys()):
                return ([map_diff[diff], index])
            map_diff[i] = index
        return ([])


arr = list(map(int, (i for i in sys.argv if "main.py" not in i)))
target = int(input())
sol = Solution()
res = sol.twoSum(arr, target)
print(res)
print("res[0] = %i" % (arr[res[0]]))
print("res[1] = %i" %arr[res[1]])