#!/usr/bin/env python3

class NumArray:

    def __init__(self, nums: list[int]):
        self.arr = nums
        self.sum = sum(nums)
        self.size = len(nums)

    def sumRange(self, left: int, right: int) -> int:
        if (right - left - 1 > self.size // 2):
            return self.sum - sum(self.arr[right + 1:] + self.arr[0:left])
        return sum(self.arr[left:right + 1])


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(5,5))
# param_1 = obj.sumRange(left,right)