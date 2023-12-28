#!/usr/bin/env python

class Solution:

    def mergeOnes(self, target : str, to_see : list, seen : set,s : str):
        res = 0
        index = -1
        for i in range(len(target) - 1):
            index+=1
            if target[i] == "1" and target[i+1] == "1" and int(s[index] + s[index+1]) <= 26:                
                tmp = target[0:i] + "2" + target[i+2:]
                if tmp in seen:
                    continue
                to_see.append(tmp)
                seen.add(tmp)
                res = 1
#        print("ouahhhhhhh\n\n\n\n",to_see)
        return res

    def isDecodable(self, s : str, mirror : str ,dic : dict) -> int:
        size = len(s)
        index_m = 0
        index_s = 0

        while index_s < size:
            if mirror[index_m] == "1":
                if not s[index_s] in dic:
                    return 0
            elif mirror[index_m] == "2":
                if not s[index_s] + s[index_s + 1] in dic:
                    return 0
                index_s += 1
            index_m+=1
            index_s += 1
        return 1

    def numDecodings(self, s: str) -> int:
        ans = 0
        dic = {str(i) : chr(64 + i) for i in range(1,27)}
        seen = set()
        to_see = ["1" * len(s)]
        i = 0
        while (1):
            contin = 0
            size = len(to_see)
            while i < size:
                contin = max(contin, self.mergeOnes(to_see[i],to_see, seen,s))
                i+=1
            if contin == 0:
                break
        for i in to_see:
            ans += self.isDecodable(s, i, dic)
#        print(to_see)
        return ans
    
sol = Solution()

s = "111111111111111111111111111111111111111111111"
s = "111111111111111111111111111111111111111111111"
s = "2611055971756562"
s='1111167821111112123114111111'
print(sol.numDecodings(s))