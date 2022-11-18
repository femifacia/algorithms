#!/usr/bin/env python3

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        res = ""
        for i in range(len(arr)):
            arr[i] = arr[i][-1::-1]
        return " ".join(arr)