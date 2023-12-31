#!/usr/bin/env python

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i,j = -1,-1
        size1 = len(word1)
        size2 = len(word2)
        tmp_size1 = 0
        tmp_size2 = 0
        while i < size1 and j < size2:
            if tmp_size1 == 0:
                i+=1
                tmp_size1 = len(word1[i]) if i < size1 else 0
            if tmp_size2 == 0:
                j+=1
                tmp_size2 = len(word2[j]) if j <  size2 else 0
            if tmp_size1 == 0 or tmp_size2 == 0:
                break
            if word1[i][-tmp_size1] != word2[j][-tmp_size2]:
                return False
            tmp_size1-=1
            tmp_size2-=1
        if i < size1 or j < size2:
            return False
        return True