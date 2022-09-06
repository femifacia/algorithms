#!/usr/bin/env python3

import sys
from typing import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        #counter create a map which has a keys, element countained in the iterator object 
        # gaved in parameter durning creation
        #the value for each key is the number of occurence of this
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return (-1)


sol = Solution()
print(sol.firstUniqChar(sys.argv[1]))