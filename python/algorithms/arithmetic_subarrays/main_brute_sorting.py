#!/usr/bin/env python

class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ans = []
        mem = {}
        for a,b in zip(l,r):
            tmp = []
            if (a,b) in mem:
                ans.append(mem[(a,b)])
                continue
            tmp = nums[a:b+1]
            tmp.sort()
            i = 1
            size = len(tmp)
            while i < size:
                if tmp[i] - tmp[i-1] != tmp[1] - tmp[0]:
                    break
                i += 1

            if i < size:
                ans.append(False)
            else:
                ans.append(True)
            mem[(a,b)] = ans[-1]
        return ans