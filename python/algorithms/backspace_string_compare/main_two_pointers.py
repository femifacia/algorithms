#!/usr/bin/env python3

import sys

# complexity
# time O(n) worst case (n == len of taller string)
# space O(1) 

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        #just intuition.

        #I started by the end of the two string

        # when I saw backspace I just skipped them

        #if I found two differents chars I return false cause these chars could not be erased

        s_pointer = len(s) - 1
        t_pointer = len(t) - 1
        s_backspace = 0
        t_backspace = 0

        while (s_pointer >= 0 and t_pointer >= 0):
            while (s[s_pointer] == '#' and s_pointer >= 0):
                s_pointer -= 1
                s_backspace += 1
            while (t[t_pointer] == '#' and t_pointer >= 0):
                t_pointer -= 1
                t_backspace += 1
            while (s_pointer >= 0 and s_backspace > 0 and s[s_pointer] != "#"):
                s_backspace -= 1
                s_pointer -= 1
            while (t_pointer >= 0 and t_backspace > 0 and t[t_pointer] != "#"):
                t_backspace -= 1
                t_pointer -= 1
            if t_pointer < 0 and s_pointer < 0:
                return True
            if t_pointer >= 0 and t[t_pointer] == "#":
                continue
            if s_pointer >= 0 and s[s_pointer] == "#":
                continue
            elif t_pointer < 0 or s_pointer < 0:
                return False
            if s[s_pointer] != t[t_pointer]:
                return False
            s_pointer -= 1
            t_pointer -= 1
        remaining_string, index, backspace = (s, s_pointer, s_backspace) if s_pointer > t_pointer else (t, t_pointer, t_backspace)
        while (index >=0):
            while (remaining_string[index] == '#' and index >= 0):
                backspace += 1
                index -= 1
            while (index >= 0 and backspace > 0 and remaining_string[index] != "#"):
                backspace -= 1
                index -= 1
            if index >= 0 and remaining_string[index] != "#":
                return False
        return True
    
sol = Solution()
print(sol.backspaceCompare(sys.argv[1], sys.argv[2]))


