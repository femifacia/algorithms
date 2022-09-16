#!/usr/bin/env python3

import sys


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)
        haystack_size = len(haystack)
        if (needle_size > haystack_size):
            return -1
        lps = [0] * needle_size
        i = 0
        j = 1
        #en premier lieu on va initialiser le lps
        #lps est un tableau d'entier ,length prefix suffix
        #a un indix i, lps[i] contient la taille du prefix qui est aussi un sufix a la chaine needle[0:i+1]
        while (j < needle_size):
            if needle[i] != needle[j] and i == 0:
                j+=1
            elif needle[i] == needle[j]:
                lps[j] = i + 1
                i+=1
                j+=1
            else:
                i = lps[i - 1]
        i = j = 0
        while (i < haystack_size and j < needle_size):
            print(i, j) 
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            elif haystack[i] != needle[j] and j != 0:
                j = lps[j - 1]
            else:
                i+=1
        print(needle)
        print(lps)
        print(i - needle_size, j)

        return (i - needle_size if j == needle_size else -1)

sol = Solution()
print(sol.strStr(sys.argv[1], sys.argv[2]))