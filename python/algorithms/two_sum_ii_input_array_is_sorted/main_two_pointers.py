#!/usr/bin/env python3


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        #we start with 
        # left = 0 (left points to the min value of the array) 
        # right = len(numbers) - 1 (right points to the max value of the array)
        left = 0
        right =  len(numbers) - 1
        # we continue until left < right but in fact we could just put while 1 cause the exercise
        # guarentee us to have one solution 
        while left < right:
            # if numbers[left] == numbers[right] we done 
            if  numbers[left] + numbers[right] == target:
                break
            # if the sum of the numbers[left] and numbers[right] is lower than target,
            # it means we are in loss of power
            # because numbers right is maximal, to have more power or a higher sum
            # we have to increment left
            if numbers[left] + numbers[right] < target:
                left += 1
            # in the other case, we have to decrease the power so we reduce our right
            else:
                right -= 1
        return [left + 1, right + 1]


sol = Solution()
numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers, target))