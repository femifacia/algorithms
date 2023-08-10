#!/usr/bin/env python3

class Solution:

    def canMakePair(self, nums, target, p) -> bool :
        # This function return true if it finds p pair with a difference lower or equal to target

        # the variable count will contain the number of pair with a difference lower or equal to target
        count = 0
        i = 0
        while i + 1 < self.size:
            if nums[i + 1] - nums[i] <= target:
                #when we find a couple with a difference lower or equal to target, we do i+=2

                # i+=2 == i += 1 on this scope because at the end of the while loop, i is always increasing
                # by 1
                # 
                # We do this because the problem told us to not have the same index two time on the couples
                # selected.
                # 
                # So, if it worked with (i, i+1), the next couple we will have to be looking is (i + 2, i + 3)
                # hence the need to do i+=2  
                count += 1
                i+=1
            if count == p:
                # if we found p couple, we can then return true
                return True
            i+=1
        return False

    def minimizeMax(self, nums: list[int], p: int) -> int:
        if p == 0:
            return 0
        # We will do a binary search, so let's sort the array
        nums.sort()
        self.size = len(nums)
        # We will do a binary Search through 0 and the max absolute difference on the array
        left,right = 0, nums[-1] - nums[0]
        while left < right:
            # this way to calculate the mid avoid having the problem of reaching the limit of an int
            mid = left + ((right - left) // 2)
            # at each difference, we will check if we can make p pair of absolute differences lower or
            # equal to p
            # 
            # If so, it means we could make maybe p couples but with a lower difference as target 
            if self.canMakePair(nums, mid, p):
                right = mid
            # Otherwise, we have to increase our target difference to see now if we can have p pair
            else:
                left = mid + 1
        # We return the lower difference found that leads us to p
        return left

sol = Solution()
p = 3
nums = [3,4,2,3,2,1,2]
print(sol.minimizeMax(nums, p))