#!/usr/bin/env python3

from bisect import bisect_right
from bisect import bisect_left

class Solution:

    def findLower(self, nums : list[int], i : int) -> int:
        return -1

    def findGreater(self, nums : list[int], i : int) -> int:
        index  = bisect_right(nums, i)
#        print(index,i)
        if index == len(nums):
            return -1
        return nums[index]
    def transformArray(self, arr1: list[int], arr2: list[int], dp : list[int], start : int, notNew = 0):
        i = start
        while i > 0 and dp[i] != 0:
            i-=1
        ans = dp[i]
        dp[start] = max(ans, notNew)
#        arr2.sort()
#        print(arr2)
#        print("let's start", start)
        for i in range(start, len(arr1)):
#            print(arr1[i])
#            print(arr1)
#            print("ok",i)
            if i + 1 < len(arr1) and arr1[i] > arr1[i+1]:
                if i - 1 >= 0:
                    elm = self.findGreater(arr2, arr1[i - 1])
                else:
                    elm = arr2[0]

#                print(elm)
#                if (elm == -1) or elm > arr1[i+1]:
                if (elm == -1) :

                    return (-1, i)
                arr1[i] = elm
                ans+=1
                dp[i] = ans
            elif i + 1 < len(arr1) and arr1[i] == arr1[i + 1]:
                if i == 0:
#                    print('ok')
                    if arr2[0] < arr1[i]:
                        ans+=1
                        arr1[0] = arr2[0]
                        dp[0] = ans
                        continue
                if i - 1 >= 0:
                    elm = self.findGreater(arr2, arr1[i-1])
#                    print('bouhw',elm,arr1)
                    if elm != -1 and elm < arr1[i]:
                        ans += 1
                        dp[i] = ans
                        arr1[i] = elm
                        continue
                elm = self.findGreater(arr2, arr1[i+1])
                if elm == -1 or arr1[i] <= elm:
                    return (-1, i + 1)
                ans +=1
                arr1[i+1] = elm
                dp[i+1] = ans
            elif i - 1 >= 0 and arr1[i] == arr1[i - 1]:
                elm = self.findGreater(arr2,arr1[i])
                if elm == -1:
                    return (-1,i)
                arr1[i] = elm
                ans+=1
                dp[i] = ans
            elif i - 1 >= 0 and arr1[i - 1] > arr1[i]:
                elm = self.findGreater(arr2, arr1[i - 1])
                if elm == -1:
                    return (-1,i)
                arr1[i] = elm
                ans +=1
                dp[i] = ans
#        print(arr1)
        return (ans,0)
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        dp = [0] * len(arr1)
        count = 0
        index = 0
        arr2.sort()
        arr1_copy = arr1[:]
        notn = 0
        while count < 10:
            print('before', arr1)
            print('before', arr2)
            ans = self.transformArray(arr1, arr2,dp,index,notn)
            print('after', arr1)
            print(dp)
            if ans[0] != -1:
                return ans[0]
#            print(ans)
            index = ans[1]
            notn = 1
            dp[index] = 1
#            print("dp",dp)
            while index > 0 and dp[index] != 0:
                index-=1
            dp = dp[0:index+1] + ([0] * (len(arr1) - index))
            arr1 = arr1[:index + 1] + arr1_copy[index+1:]
            if index > 0:
                arr1[index] = self.findGreater(arr2, arr1[index - 1])
            else:
                arr1[index] = arr2[0]
            count +=1

        return -1


sol = Solution()
arr1 = [1,4,3,5]
arr2 = [-9,-8,4,2,1,1,6]
arr1 = [1,3,3,4,4,5,6]
arr2 = [1,2,9]
arr1 = [1,5,3,6,7]
arr2 = [4,3,1]
arr1 = [1,5,3,6,7]
arr2 = [1,6,3,3]
arr1 = [0,11,6,1,4,3]
arr2 = [5,4,11,10,1,0]
arr1=[5,16,19,2,1,12,7,14,5,16]
arr2=[6,17,4,3,6,13,4,3,18,17,16,7,14,1,16]
arr1 = [9,18,3,8,21,6,7,2,7,28,23,16,33,2,25,14,15]
arr2 = [13,2,15,30,31,30,9,10,7,30,31,4,33,10,25,28,19,6,15,6,19,30,25,14,7,28,23,20,1,2,25,16]
arr1 = [19,18,7,4,11,8,3,10,5,8,13]
arr2 = [13,16,9,14,3,12,15,4,21,18,1,8,17,0,3,18]
print(sol.makeArrayIncreasing(arr1,arr2))