#!/usr/bin/env python3

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        limit  = 32
        for i in range(limit):
            if (1 << (limit - i - 1)) & n:
                res = res | (1 << i)
        return res
sol = Solution()
n = 0b01101
n =0b00000010100101000001111010011100
print(bin(n))
print(bin(sol.reverseBits(n)))