#!/usr/bin/env python3

class MedianFinder:

    def __init__(self):
        self.heap = [None]
        self.rank = {}
        self.size = 1

    def up(self, i) -> None:
        elm =self.heap[i]
        while i > 1 and elm < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        self.heap[i] = elm
        self.rank[elm] = i

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        self.rank[num] = self.size
        self.up(self.size)
        self.size += 1

    def findMedian(self) -> float:
        #self.arr.sort()
        print(self.heap)
        print(self.rank)
        if ((self.size - 1) % 2 == 0):
            print(self.size, 'div 2', (self.size- 1) // 2)
            return ((self.heap[(self.size - 1) // 2] + self.heap[((self.size- 1) // 2) + 1]) / 2)
        return (self.heap[(self.size - 1) // 2 + 1])

med = MedianFinder()
med.addNum(6)
print(med.findMedian())
med.addNum(10)
print(med.findMedian())
med.addNum(2)
print(med.findMedian())