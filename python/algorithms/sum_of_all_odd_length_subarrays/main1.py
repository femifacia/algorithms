#!/usr/bin/env python3

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        res = 0
		#for this exercise we're gonna to caluculate the number of time where arr[i] occure in all subbarray
        # we can create from arr.
        for i in range(n):
            # to do so, we will calculate the number of subarray which start with this index
            # it is equal to the size - the index 
            start = n - i
            # after that we calculate the number of subarrays which end with our index
            end = i + 1
            #the number of subbarray we can make with our index is start * end
            number_occured = (start * end)
            #so to find the number of subbarray of odd length we divid it by 2
            #if the number of occurence is odd we add to the result of the division 1
            # number_occured & 1 is equal to 0 if the first bit is set to 1 which means it is odd
            number_occured = number_occured // 2 if number_occured & 1 == 0 else (number_occured // 2) + 1
            # then we add the arr[i] multiplied by the number of times it occurs
            res += arr[i] * (number_occured)
        return res