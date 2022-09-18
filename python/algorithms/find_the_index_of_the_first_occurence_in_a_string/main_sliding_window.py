#!/usr/bin/env python3

import sys


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)
        haystack_size = len(haystack)
        if (needle_size > haystack_size):
            return -1
        #so here we look at each string from i ... to needle size + i to check if it corresponds to needle
        for i in range(0, haystack_size - needle_size + 1):
            print(i)
            if (haystack[i : needle_size + i] == needle):
                return(i)
        return (-1)

sol = Solution()
print(sol.strStr(sys.argv[1], sys.argv[2]))