#!/usr/bin/env python3

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")