#!/usr/bin/env python3

class NumArray:

    def __init__(self, nums: list[int]):
        self.arr = nums
        self.size = len(self.arr)
        self.middle_size = self.size // 2
        #we do the sum of all elements
        self.total = sum(self.arr)

    def update(self, index: int, val: int) -> None:
        #we remove the val of the element we are gonna update
        self.total -= self.arr[index]
        self.arr[index] = val
        #we add its new val
        self.total += val

    def sumRange(self, left: int, right: int) -> int:
        #if we have more element to sum than the half of the arr size, we will remove the left side and the right
        #side of the sum and push it
        if (right - left +1 > self.middle_size):
            res = self.total
            left -=1 
            #we remove the left size on the sum
            while (left >= 0):
                res -= self.arr[left]
                left-=1
            right += 1
            #we remove the right size on the sum
            while (right < self.size):
                res -= self.arr[right]
                right += 1
            return res
        #here we do the sum if there is less element to add than the left and right side we add it
        #manually
        res = self.arr[left]
        left += 1
        while (left <= right):
            res += self.arr[left]
            left +=1
        return res


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