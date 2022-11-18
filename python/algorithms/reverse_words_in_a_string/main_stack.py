#!/usr/bin/env python3

class Solution:
    def reverseWords(self, s: str) -> str:
        st = []
        tmp = ""
        i = len(s) - 1
        while (i >= 0):
            while (i >= 0 and s[i] == " "):
                i-=1
            while (i >= 0 and s[i] != " "):
                tmp = s[i] + tmp
                i-=1
            if tmp:
                st.append(tmp)
            tmp = ""
        return " ".join(st)