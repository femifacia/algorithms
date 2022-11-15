#!/usr/bin/env python3

import sys

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in s:
            if st and st[-1] == i:
                st.pop()
            else:
                st.append(i)
        return "".join(st)

sol = Solution()
print(sol.removeDuplicates(sys.argv[1]))