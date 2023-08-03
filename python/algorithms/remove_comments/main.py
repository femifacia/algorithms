#!/usr/bin/env python3

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        res = []

        tmp = ""
        comment_opened = 0
        for line in source:
            i=0
            while i < len(line):
                if line[i] == '/' and i + 1< len(line):
                    if line[i+1] == '/' and not comment_opened:
                        break
                    if line[i+1] == '*' and not comment_opened:
                        comment_opened = 1
                        i+=2
                        continue
                    elif not comment_opened:
                        tmp += '/'
                elif comment_opened != 1:
                    tmp += line[i]
                if line[i] == '*' and i + 1 < len(line) and line[i+1] == '/' and comment_opened:
                    comment_opened = 0
                    i+=1
                i+=1
                print(tmp,'---')
            if tmp and comment_opened != 1:
                res.append(tmp)
                tmp = ""
        if tmp:
            res.append(tmp)
            tmp = ""
        return res
    
sol = Solution()

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source = ["a/*comment", "line", "more_comment*/b"]
source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
source = ["a//*b/*/c","blank","d/*/e/*/f"]
source = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
source = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
source = ["k*/"]
res = sol.removeComments(source)
[print(i) for i in source]
print('!!!--------!!!!')
[print(i) for i in res]