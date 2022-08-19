#!/usr/bin/env python3

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version not in range(40)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while (left < right):
            mid = (right + left) // 2
            print(mid)
            if ( isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return (left)

sol = Solution()
print(sol.firstBadVersion(45))