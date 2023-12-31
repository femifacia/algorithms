#!/usr/bin/env python

# DO NOT WORKKKKKKKKKK

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        left_seen = {}
        right_seen = {}
        i = 0
        j = len(s) - 1
        while (i < j):
            if s[i] in right_seen or s[j] in left_seen:
                if s[i] in right_seen:
                    return right_seen[s[i]] - i - 1
                return j - left_seen[s[j]] - 1
            left_seen[s[i]] = i
            right_seen[s[j]] = j
            i += 1
            j -= 1
        return -1