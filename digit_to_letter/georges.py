#!/usr/bin/env python3
import sys

class Solution:
    def numberToWords(self, num: int) -> str:
        rank = {0: "", 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}
        numbers = {
            0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }
        copystr = ""
        for i, char in enumerate(str(num)[::-1]):
            copystr += char
            if (i+1)%3 == 0 and (i+1) < len(str(num)[::-1]):
                copystr += "*"
        nbrlist = copystr[::-1].split("*")
        result = ""
        for i, elem in enumerate(nbrlist):
            elem_rank = len(nbrlist) - i - 1
            elem = str(int(elem))
            for j, digit in enumerate(elem):
                if len(elem) - j == 3:
                    result += numbers[int(digit)]
                    result += " "
                    result += "Hundred"
                elif len(elem) - j == 2:
                    if int(digit) >= 2:
                        result += (numbers[int(digit)*10])
                    else:
                        result += numbers[int(digit+elem[j+1])]
                        result += " "
                        break
                else:
                    result += (numbers[int(digit)])
                result += " "
            result += rank[elem_rank]
            result += " "

        return (result.strip())

if (len(sys.argv) == 1):
    exit(84)
sol = Solution()
print(sol.numberToWords(int(sys.argv[1])))
