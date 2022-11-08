#!/usr/bin/env python3

class Solution:

    def count1Bits(self, num : int) -> int:
        ans = 0
        for i in range(32):
            ans += (((1 << i) & num)) != 0 
        return ans

    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort()
        arr.sort(key=self.count1Bits)
        return arr

sol = Solution()
arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr = [0,1,2,3,4,5,6,7,8]
print(sol.sortByBits(arr))