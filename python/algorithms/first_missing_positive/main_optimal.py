#!/usr/bin/env python3

# time O(3n) = O(n)
# space O(1)

class Solution:
    def firstMissingPositive(self, nums):
        # the solution is in the interval [1, len(nums) + 1]
        # so we will transform nums to a set and request for the numbers from 1 to len(nums + 2)
        # to see which numb is not in the set

        # cause the request of finding an elm in a set is constant we have an 0(n) solution

        # but we won't init a hashset. We will transform our nums list into a "hashset" without any cast
        # or memory allocation

        # we are first gonna to transform all negatives values into 0 because they won't be useful for us
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # then we will use negative to confirm the presence of a number in the array
        # indeed, to instantly check if a val number is in our array we will change the value of
        # nums[number - 1] into a negative value
        # 
        # So if we want to know if a value val is in our array we will just check if nums[val - 1] is negative
        # If it is, it means val is in our array. Else not  

        for i in range(len(nums)):
            number = abs(nums[i])
            # at this level, all negative numbers we could encounter are in the array beacause they
            # ensure the existance of other positive numbers in the array. 

            # Remember, we have replaced each original negative number by a 0

            if number <= len(nums) and number != 0:
                # if the original number is greater than the size of the array it means that this number
                # cannot be our solution. So we can ignore it
                # 
                # if the number we are gonna to transform in negative is 0, we replace it by -number or we could
                # have replaced it by a value greater than len(nums) because it could not be our solution.
                # Indeed if we replace a 0 val by -number, when we will find the index of the
                # number we have transformed, we will just remark that number is in the box and that is true.
                # We don't modify the array.
                # We do this to not transform the array and the solution
                nums[number - 1] = -1 * abs(nums[number - 1]) if nums[number - 1] != 0 else -number
                # we could have done the following line 
#                nums[number - 1] = -1 * abs(nums[number - 1]) if nums[number - 1] != 0 else -(len(nums) + 1)
        
        # at the end we check the first element which is not on the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1


        
sol = Solution()
arr = [1,2,4,3,5,0,0,9,6,7,10,11,8,-13,13,12]
arr = [0,1,2]
print(sol.firstMissingPositive(arr))