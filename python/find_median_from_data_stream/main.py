#!/usr/bin/env python3

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.middle = 0
        self.size = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.size += 1

    def findMedian(self) -> float:
        self.arr.sort()
        if (self.size % 2 == 0):
            #print(self.size, 'div 2', self.size // 2)
            return ((self.arr[self.size // 2] + self.arr[self.size // 2 - 1]) / 2)
        return (self.arr[self.size // 2])

med = MedianFinder()
med.addNum(6)
print(med.findMedian())
med.addNum(10)
print(med.findMedian())
med.addNum(2)
print(med.findMedian())
