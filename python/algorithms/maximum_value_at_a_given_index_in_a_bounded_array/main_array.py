#!/usr/bin/env python3

# to slowwww 

import sys

class Solution:

    def adder(self, array, index):
        print(array, index)
        self.sum+=1
        if self.sum > self.limit:
            array[self.index] = self.last
            return
        array[index] += 1
        if index - 1 >= 0 and abs(array[index] - array[index - 1]) > 1:
            self.adder(array, index - 1)
        if self.sum > self.limit:
            array[self.index] = self.last
            return
        if index + 1 < self.n and abs(array[index] - array[index + 1]) > 1:
            self.adder(array, index + 1)



    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        i = maxSum // n
        array = [i] * n
        self.n = n
        self.index = index
        self.sum = n
        self.limit = maxSum
        self.ans = 1
        while (self.sum < maxSum):
            self.last = array[index]
            self.adder(array, index)
            self.ans = array[index]
        print(array)
        return self.ans


sol = Solution()
n = int(sys.argv[1])
index = int(sys.argv[2])
maxSum = int(sys.argv[3])
print(sol.maxValue(n,index,maxSum))