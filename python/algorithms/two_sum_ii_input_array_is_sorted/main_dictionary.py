#!/usr/bin/env python3

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(numbers)):
            ret = target - numbers[i]
            if ret in dic:
                return [dic[ret], i + 1]
            dic[numbers[i]] = i + 1


sol = Solution()
numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers, target))