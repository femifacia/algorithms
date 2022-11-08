#!/usr/bin/env python3

from functools import cmp_to_key

# be carefull !!!!!!!!!!!!!!dont work

class Solution:

    def count1Bits(self, num : int) -> int:
        ans = 0
        for i in range(32):
            ans += (((1 << i) & num)) != 0 
        return ans
    
    def compare(self, a : int, b : int) -> int:
        aBits = self.count1Bits(a)
        bBits = self.count1Bits(b)
        print(aBits, bBits)
        if (aBits == bBits):
            return a < b
        return bBits > aBits

    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=cmp_to_key(self.compare))
        return arr

sol = Solution()
arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr = [0,1,2,3,4,5,6,7,8]
print(sol.sortByBits(arr))