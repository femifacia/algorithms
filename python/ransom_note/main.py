#!/usr/bin/env python3

import sys

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return (False)
        return True

sol = Solution()
print(sol.canConstruct(sys.argv[1], sys.argv[2]))