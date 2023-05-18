#!/usr/bin/env python3

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        left = [0,0]
        right = [height-1,width-1]
        while left[0] <= right[0]:
            mid = (left[0] + right[0]) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left[0] = mid + 1
            else:
                right[0] = mid - 1
        m = right[0]
        while left[1] <= right[1]:
            mid = (left[1] + right[1]) // 2
            if matrix[m][mid] == target:
                return True
            if matrix[m][mid] < target:
                left[1] = mid + 1
            else:
                right[1] = mid - 1
        return False

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))