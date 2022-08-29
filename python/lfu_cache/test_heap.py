#!/usr/bin/env python3

import heapq

li = [1,9,8,5,3]
sah = heapq.heapify(li)
heapq.heappop(li)
print(li)