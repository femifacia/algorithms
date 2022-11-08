#!/usr/bin/env python3

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #the result array
        res = [-1] * len(nums1)
        #this is a hash map which for each element in nums1 associate its index
        #we do this because, in the result array when we find a greater element, to put it to its right place
        #we need to know the index of the number for whom it is greater
        index_dic = {elm : i for i, elm in enumerate(nums1)}
        #for this exercise we will use a stack, a decreasing stack
        st = []
        #our solution will be a one pass solution
        for i in range(nums2):
            current = nums2[i]
            #we check if our current element is greater than the last element on the stack if the stack is not
            # empty obviously
            while st and current > st[-1]:
                #if it is we pop it and assignate in our res that the next greater element of this element
                #is current.
                val = st.pop()
                res[index_dic[val]] = current
                #then we will continue untill all element lower than our current are checked

            #if our current is in nums1 we add it to the stack
            if current in nums1:
                st.append(current)
            
            #if nums1 is [7,4,5,9,1,3] and our arr is [0,2,7,-5,4,5,9,1,3]
            # at the first loop our current is 0 and our stack empty
            # 0 is not in nums1 so we don't add it to our stack
            # same for 2
            # then when we are on 7, our stack is still empty but 7 is in nums1
            # so we add it to the stack
            # after this we are facing -5
            # -5 is not greater than 7 so we contiue
            # same for 4 but we add it to our stack because it is ni nums1
            # we got 5. 5 is greater than our top value on the stack (4)
            # so we pop 4 and tell greater of 4 is 5
            # than we continue. But 5 is not greater than 7 so we stop it right now
            # at the end element remained on stack have the value assigned to their index in the res array to -1 
        return res