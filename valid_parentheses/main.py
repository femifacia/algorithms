#!/usr/bin/env python3


import sys

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        nbr_str = str(num)
        max = ""
        for i in range (0, 10):
            string = str(i) * 3
            if string in nbr_str:
                max = i
            #print(i)
        if (max == ""):
            return ("")
        return ((str(max) * 3))
        
so = Solution()
print(so.largestGoodInteger(int(sys.argv[1])))