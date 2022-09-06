#!/usr/bin/env python3

import array
import sys

class Solution:
    def groupAnagrams(self, strs):
        anagram_dic = {}
        for i in strs:
            signature = "".join(sorted(i))
            if (signature in anagram_dic.keys()):
                anagram_dic[signature].append(i)
            else:
                anagram_dic[signature] = [i]
        anagram_arr = [anagram_dic[i] for i in anagram_dic.keys()]
        return anagram_arr

if (len(sys.argv) != 2):
    print("Enter a test file", file=sys.stderr)
    exit(1)
fd = open(sys.argv[1], 'r')
arr = [i  for i in fd.read().split('\n') if (i != "")]
fd.close()
print(arr)
sol = Solution()
print(sol.groupAnagrams(arr))