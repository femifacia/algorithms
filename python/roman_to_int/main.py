#!/usr/bin/env python3
class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        s = s.replace("IV", "A")
        s = s.replace("IX", "B")
        s = s.replace("XL", "E")
        s = s.replace("XC", "F")
        s = s.replace("CD", "G")
        s = s.replace("CM", "H")
        dic = {
            "I" : 1,
            "A" : 4,
            "V" : 5,
            "B" : 9,
            "X" : 10,
            "E" : 40,
            "F" : 90,
            "G" : 400,
            "H" : 900,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        for i in s:
            count += dic[i]
        #print(s)
        return (count)