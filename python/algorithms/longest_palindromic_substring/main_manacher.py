#!/usr/bin/env python3

import sys

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # as you see we will use a string called t
        # t will be our old s string but delimited by ^# and #$
        # Between each character of s there will be #
        # for example if s == "feemi" t will be equal to ^#f#e#e#m#i#$
        # by this way it will be easy to deal with odd or even palindromes 
        # for example at the position 2 of t (f) the length of the highest palindrome that can be found 
        # is 1 cause f is sourrounded by # #
        # we will use this way to find all palindrome and their length
        t = "^#" + "#".join(s) + "#$"
        size_t = len(t)
        # p will contain for an index i the radius of the longest palindrome which can be find from this index
        # so from i - p[i] to i + p[i] we are facing a palindrome
        p = [0] * size_t
        d = c = 0
        # c will be our center
        # and d the distance of the highest palindrome we can found at c index
        for i in range(1, size_t - 1):
            mirror = 2 * c - i # it is the index of the mirror of i by c. It is c - (i - c) cause i > c so
            # it can be resumed at 2 * c - i
            # given mirror the mirror of i by c, there is a relation between p[mirror] and p[i]
            # if i + p[mirror] <= d we can initalize p[i] with the value of p[mirror]
            if i + p[mirror] <= d:
                p[i] = p[mirror]
            #we will make growth the palindrome
            while (t[i + 1 + p[i]] == t[i - 1 - p[i]]):
                p[i] += 1
            #we will adjust the center if necessary  
            if i + p[i] > d:
                d = i + p[i]
                c = i
        (k, i) = max((p[i], i) for i in range(1, size_t - 1))
        # k is the size of the longest palindrome
        # i is the index of the longest palindrome
        # the longuest palindrome start at (i - k) // 2 and finish at ((i + k) // 2 )
        #so we return the string going from the start to the end
        return s[(i- k) // 2 : (i + k) // 2]

sol = Solution()
print(sol.longestPalindrome(sys.argv[1]))