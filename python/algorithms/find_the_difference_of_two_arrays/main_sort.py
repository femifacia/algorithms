#!/usr/bin/env python3

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans1 = []
        ans2 = []

        nums1.sort()
        nums2.sort()
        i,j,size1,size2=0,0,len(nums1),len(nums2)
        while i < size1 and j < size2:
            while i + 1 < size1 and nums1[i] == nums1[i + 1]:
                i+=1
            while j + 1 < size2 and nums2[j] == nums2[j + 1]:
                j+=1
            if nums1[i] < nums2[j]:
                ans1.append(nums1[i])
                i+=1
            elif nums2[j] < nums1[i]:
                ans2.append(nums2[j])
                j+=1
            else:
                i+=1
                j+=1
        while i < size1:
            while i + 1 < size1 and nums1[i] == nums1[i + 1]:
                i+=1
            ans1.append(nums1[i])
            i+=1
        while j < size2:
            while j + 1 < size2 and nums2[j] == nums2[j + 1]:
                j+=1
            ans2.append(nums2[j])
            j+=1
        return [ans1, ans2]