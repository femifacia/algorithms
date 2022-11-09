#!/usr/bin/env python3

class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixSum = nums
        #we will calculate the prefix sum of each element
        for i in range(1, len(nums)):
            self.prefixSum[i] += self.prefixSum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(5,5))
# param_1 = obj.sumRange(left,right)