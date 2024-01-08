#!/usr/bin/env python

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0

        last_security = -1
        for i in bank:
            actual_security = 0
            for j in i:
                if j == '1':
                    actual_security += 1
            if actual_security and last_security > 0:
                res += (actual_security * last_security)
                last_security = actual_security
            elif last_security == -1 and actual_security:
                last_security = actual_security
        return res