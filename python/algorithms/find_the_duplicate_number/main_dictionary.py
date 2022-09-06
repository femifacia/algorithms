#!/usr/bin/env python3

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dic = {}
        for i in nums:
        #if i has already been seen on the fic we found our dupplicate
            if i in dic:
                return (i)
        #else we append it to the dictionary
            dic[i] = 1
        return (-1)