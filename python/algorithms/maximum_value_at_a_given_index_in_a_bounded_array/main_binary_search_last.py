#!/usr/bin/env python3

# to slowwww 

import sys
#
#Binary Search (Thanks God I would turn crazy)
#Complexity
#Time: O(logn)
#Space: O(1)
#So, If you are attentive, an array with the index maximized and which respect constraints would look like: arr = [1,2,3,*4*,3,2] .
#
#arr[index] is maximized. And elements above it are decreasing by 1. So we can use binary search to try to find a number which will respect the constraints and keep our arr[index] maximized.
#
#First of all, we know that answer is ≥ 1. So we know our left. We also know that answer will never go after maxSum - n . You can think about it but it is true. So we have our right.
#
#We will calculate the mid of our boundaries. For this mid we will see if it respects the constraints, which means if having an array with arr[index] = mid and with decreasing number around index will let us have an array with sum ≤ maxsum.
#
#How to calculate the sum without building the array
#Let’s take an example:
#
#arr = [1,1,1,2,3,4,5,4,3]
#
#We can see that we have two parts above index; left part and right part
#
#left part (including index itself) is made by leading 1 (1,1) and sum of elements before arr[index] (here the sum of elements before 5) (1,2,3,4,5). So if we find a formula to calculate number of leading one and the sum of consecutive elements before arr[index], we could calculate the sum without building the array
#
#This is the formula of the leading 1
#
#left_leading_1 = max(0, index - mid + 1)
#Indeed, if index - mid + 1 < 0 it means there is no leading 1, so left_leading_1 would be equal to 0
#
#this is the formula to calculate the sum of all consecutive elements coming before n (n included)
#
#summ = (n * (n + 1) / 2)
#Even if n is odd; because of the + 1, we ensure that the result of n * (n+1) / 2 will a whole number
#
#Now, let’s look after the right part. It is constituted just as the previous one; with a number of leading 1 and with sum of consecutive
#
#This is the formula to calculate number of leading 1 at the right
#
#right_leading_1 = max(0, n - mid-index)
#In the example above there are no leading 1
#
#Now, about the sum of consecutive numbers, we see that the sequence is 5,4,3. To calculate this sum, we can just calculate the sum of all numbers < 5 and retrieve the sum of all numbers < 2.
#
#So if there is no leading 1; we could just calculate the sum of all i elements before 5
#
#After development we have this formula
#
#summ = (mid * (2 + 2 * index) - index - (index ** 2)) / 2
#With index the number of elements we want to have in our sequence
#
#To adapt it to the right sum, we could replace index by n-index-1 (the number of elements after arr[index]) in the case there would be no leading 1 on the right
#
#right_sum = (mid * (2 + 2 * (n-index-1)) - n + index +1 - ((n-index-1) ** 2)) / 2
#Then, by doing the sum of left_sum, right_sum, left_leading_1, right_leading_1and after retrieving mid of that we have the sum mid would have created if mid was our maximized solution at index.
#
#If this sum < maxSum, it means we could increase left by setting it to mid + 1. Else if sum > maxSum, we would decrease right and if sum == maxSum, it would mean we found our index.
#
#This is the code
#
class Solution:
    def calcSumForIndex(self, mid  : int,index : int, n : int) -> int:
        result = 0
        left_leading_1 = max(0, index - mid + 1)
#        print("left_sumss", left_sum)
        if (mid - index -1) > 0:
            left_sum = (mid * (2 + 2 * index) - index - (index ** 2)) / 2
        else:
            left_sum = int(mid * ((mid + 1) / 2)) + left_leading_1

        right_leading_1 = max(0, n - mid-index)
#        print("right sum",right_sum)
        if n - index < mid:
            right_sum = (mid * (2 + 2 * (n-index-1)) - n + index +1 - ((n-index-1) ** 2)) / 2
#            right_sum -= int(((mid - n + index)  * (mid - n + index + 1)) / 2)
        else:
            right_sum = int(mid * (mid + 1) / 2) + right_leading_1
            
#        print("right sum after",right_sum)
        result =  left_sum + right_sum - mid
        arr = [1] * n
        arr[index] = mid
#        print(arr, left_sum,right_sum,mid)
#        print(arr)
#        print("left sum",left_sum)
#        print("sum raw", sum(arr))
#        print("left leading ones",left_leading_1)
#        print("right leading ones", right_leading_1)
        return result




    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum - index
        ans = 1
        if n == 1:
            return maxSum

        while left <= right:
            mid = (left + right) // 2
            array_sum = self.calcSumForIndex(mid,index,n)
            if array_sum < maxSum:
                ans = mid
                left = mid + 1
            elif array_sum > maxSum:
                right = mid - 1
            else:
                return mid
        return ans


sol = Solution()
n = int(sys.argv[1])
index = int(sys.argv[2])
maxSum = int(sys.argv[3])
print(sol.maxValue(n,index,maxSum))
#print(sol.calcSumForIndex(n,index,maxSum))