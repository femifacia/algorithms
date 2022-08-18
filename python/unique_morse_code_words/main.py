#!/usr/bin/env python3

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = {}
        count = 0
        for i in words:
            morse_word = ""
            for j in i:
                morse_word += morse[ord(j) - 97]
            if (not morse_word in dic):
                dic[morse_word] = 0
                count += 1
        return (count)


sol = Solution()
arr = ["gin", "zen", "gig", "msg"]
#arr = []
print(sol.uniqueMorseRepresentations(arr))