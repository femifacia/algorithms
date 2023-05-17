#!/usr/bin/env python3

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for i in s:
            if i == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(i)
        for i in t:
            if i == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(i)
        return s_stack == t_stack
