#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]