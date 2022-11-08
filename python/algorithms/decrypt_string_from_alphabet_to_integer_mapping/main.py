#!/usr/bin/env python3

class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        #dictionary for val from 1 to 9
        dic1 = {str(i) : chr(96 + i) for i in range(1, 10)}
        #dictionary for val from 10# to 26# but I dont add #
        #it is not necessary to add #
        dic2 = {str(i) : chr(96 + i) for i in range(10, 27)}
        size = len(s)
        i = 0
        while (i < size):
            if i +2 < size:
                #if # is on i + 2
                if s[i + 2] == '#':
                #I increment ans by the correspondant of the value before # on the second dictionary
                    ans+=dic2[s[i : i + 2]]
                    i += 3
                    continue
            #if i dont enter into the previous if and don't reach the continue I just append the value of s[i]
            #which is the correspondant of dic1[s[i]]
            ans += dic1[s[i]]
            i+=1
        return ans

sol = Solution()
s= "11"
print(sol.freqAlphabets(s))