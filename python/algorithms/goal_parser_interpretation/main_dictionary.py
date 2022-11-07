#!/usr/bin/env python3

class Solution:
    def interpret(self, command: str) -> str:
        dic = {'G' : 'G', '()' : 'o', '(al)' : 'al'}
        sliding_widow = ""
        res = ""
        for i in command:
            sliding_widow += i
            if sliding_widow in dic:
                res+=dic[sliding_widow]
                sliding_widow = ""
        return res