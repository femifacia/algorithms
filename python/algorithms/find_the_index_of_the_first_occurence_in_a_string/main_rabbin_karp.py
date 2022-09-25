#!/usr/bin/env python3

import sys


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)
        haystack_size = len(haystack)
        if (needle_size > haystack_size):
            return -1
        prime = 11
        hash_s = 0
        hash_t = 0
        left = 0
        right = needle_size - 1
        #so let's implement hash_s and hash_t (hash haystack and hash needle)
        for i in range(needle_size):
            hash_s += (ord(haystack[i]) * (prime ** i))
            hash_t += (ord(needle[i]) * (prime ** i))
        while right < haystack_size:
            #if hashes are equals we compare sliding window from left to right with needle
            if (hash_s == hash_t):
                if (haystack[left : right + 1] == needle):
                    return (left)
            #we update the hash
            #we substract the value of the left char on the slinding window
            hash_s -= ord(haystack[left])
            #we divid the hash by prime
            hash_s //= prime
            #and if we are not on the end, we add the value of right + 1 char of the sliding window * (prime **(t_size - 1))
            if (right + 1 < haystack_size):
                hash_s += (ord(haystack[right + 1]) *(prime ** (needle_size - 1)))
            right += 1
            left += 1
        return (-1)

sol = Solution()
print(sol.strStr(sys.argv[1], sys.argv[2]))