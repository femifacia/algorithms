#!/usr/bin/env python3

import sys

#dont work

class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = sorted(s)
        i = 0
        size = len(s)
        print(arr)
        while i + 1 < size:
            if (arr[i] != arr[i+1]):
                return (s.index(arr[i]))
            c = arr[i]
            while (i + 1 < size and arr[i] == c):
                i+=1
        if (arr[size -1] != c):
            return(s.index(arr[size-1]))
        return (-1)


sol = Solution()
print(sol.firstUniqChar(sys.argv[1]))