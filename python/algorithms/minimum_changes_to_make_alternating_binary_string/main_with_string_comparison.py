#!/usr/bin/env python

class Solution:
    def minOperations(self, s: str) -> int:
        one,two=0,0
        ref_one = '10'
        ref_two = '01'
        index = 0
        for i in s:
            if i != ref_one[index]:
                one += 1
            if i != ref_two[index]:
                two += 1
            index += 1
            index = index % 2

        return min(two, one)