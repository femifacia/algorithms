#!/usr/bin/env python3
class Solution:
    def intToRoman(self, num: int) -> str:
        string = ""
        dic = {
            1000:{
                1:"M"
            },
            100:{
                1:"C",
                4:"CD",
                5:"D",
                9:"CM"
            },
            10:{
                1:"X",
                4:"XL",
                5:"L",
                9:"XC"
            },
            1:{
                1:"I",
                4:"IV",
                5:"V",
                9:"IX"
            }
        }
        decimal = 1
        while (decimal * 10 <= num):
            decimal *= 10
        while (decimal >= 1 and num > 0):
            quotient = int(num // decimal)
            letter = ""
            digit = 0
            #print(quotient)
#            print((dic[decimal])[1])
            if (quotient in dic[decimal]):
                letter = dic[decimal][quotient]
            else:
                for i in dic[decimal].keys():
                    if i > quotient:
                        break
                    digit = i
                #print("%i and %i and %s" %(decimal, digit, string))
                if digit > 0:
                    letter += dic[decimal][digit]
                    digit = quotient - digit
                    while (digit > 0):
                        letter += dic[decimal][1]
                        digit -= 1
            string += letter
            num = num % decimal
            decimal /= 10
        return (string)

sol = Solution()
print(sol.intToRoman(1852))