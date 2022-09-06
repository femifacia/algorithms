#!/usr/bin/env python3

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        #so becase here the value of each element won't go after len(nums)
        #we can consider values itselves as pointers
        #so we start at nums[0]
        #as the usually floyd detection we go nums[pointer]
        slow = nums[0]
        speed = nums[0]
        while 1:
        #our slow pointer will go slow = nums[slow]
        #while our speed pointer will go speed = nums[nums[speed]]
            slow = nums[slow]
            speed = nums[nums[speed]]
            if (slow == speed):
                break
        #when we found the place where there are equals, we just do as the linked list cycle II
        #we instanciate a pointer to the head (nums[0]) and wait to it to be the same than slow
        head = nums[0]
        while (head != slow):
            head = nums[head]
            slow = nums[slow]
        return (head)