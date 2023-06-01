#!/usr/bin/env python3

import sys

# Complexity

#- Time: O(nlog(n))
#- Space: O(1)



class Solution:
    def search(self, nums: list[int], target: int) -> int:
    # We have a rotated array. Let’s call the pivot of the rotation `k`. 
    # Our array is partitioned in two separated by `k`. A left part and a right part.
    #  Any number before `k` is greater than any number after `k` .
    # Depending on the position of `mid` (is mid on the left side ? or the right side ? the choice of
    #  moving on **left** (`left = mid + 1`) and moving on **right** (`right = mid - 1`) depend of some factors.
    #  I wrote those conditions depending on the position on mid on paper and tried it on leetcode

    # here we have a little difference with the previous one exercise: The existence of duplicates.

    # We have to add a condition to skip duplicates
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left] and nums[mid] == nums[right]:
                #we skip duplicates here
                left+=1
                right-=1
            elif nums[mid] > nums[right]:
                #here mid is on the left side
                if target > nums[mid]  or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else :
                #here mid is on the right side
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid-1
        return False

sol = Solution()
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = int(sys.argv[1])
print(nums)
print(sol.search(nums, target))