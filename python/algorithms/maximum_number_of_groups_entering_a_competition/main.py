#!/usr/bin/env python3

class Solution:

    def getIndexSum(self, arr, max_sum, size):
        lenn = len(arr)
        i = 0
        while (i + size <= lenn):
            j = 0
            summ = 0
            while (i + size <= lenn and j < size):
                summ += arr[i + j]
                j+=1
            if (summ > max_sum):
                return (i, max_sum)
            i+=1
        return (-1, max_sum)

    def maximumGroups(self, grades: list[int]) -> int:
        arr = sorted(grades)
        count = 1
        size = 1
        max_sum = arr.pop()
        while 1:
            index, max_sum = self.getIndexSum(arr, max_sum, size + 1)
            if (index == -1):
                break
            size += 1
            count +=1
            j = 0
            while (j < size):
                del arr[index]
                j+=1
        return (count)

sol = Solution()
print(sol.maximumGroups([10,6,12,7,3,5]))
print(sol.maximumGroups([8,8]))
print(sol.maximumGroups([8,8, 10, 15, 2]))