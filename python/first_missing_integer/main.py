#!/usr/bin/env python3

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        nbr = 1
        last_numb = 0
        for i in nums:
            if i <= 0:
                continue
            if (nbr < i):
                return nbr
            if (i == last_numb):
                continue
            last_numb = i
            nbr +=1
        return (nbr)
        