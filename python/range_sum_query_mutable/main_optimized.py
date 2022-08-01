#!/usr/bin/env python3

class NumArray:
    nums = []
    s = 0
    l = 0
    
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.s = sum(nums)
        self.l = len(nums)

    def update(self, index: int, val: int) -> None:
        self.s -= self.nums[index]
        self.nums[index] = val
        self.s += self.nums[index]

    def sumRange(self, left: int, right: int) -> int:
        if right - left > self.l // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.s - ans
        else:
            return sum(self.nums[left: right + 1])

# Your NumArray object will be instantiated and called as such:
#nums=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
nums = [9, -8]
obj = NumArray(nums)
obj.update(0,3)
print(obj.sumRange(1,1))
print(obj.sumRange(0,1))
obj.update(1,-3)
print(obj.sumRange(0,1))
param_2 = obj.sumRange(1,12)