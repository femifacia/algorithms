#!/usr/bin/env python3

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #I will start from the end to use this two pointers method
        #p1 start from the last element of nums1 array
        p1 = m - 1
        #p2 start from the last element of nums2 array
        p2 = n -1
        #index will fill nums1 starting from 0
        index = m + n - 1

        while (p1 >= 0 and p2 >= 0):
            if (nums1[p1] > nums2[p2]):
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1
        # when one pointer end, to not have to allocate new variables, I affect to nums2 the remaining array
        # If p1 > p2 it means nums1 is the remaining array so I affect its reference to nums2
        # Same for p2. I affect the value of p1
        # 
        # If it is the other case, nums2 and p2 would contain the informations of the remaining array
        # 
        # No matter the remaining array, it will always be consigned into nums2  
        if p1 > p2:
            nums2 = nums1
            p2 = p1
        while p2 >= 0:
            nums1[index] = nums2[p2]
            p2 -=1
            index -= 1 