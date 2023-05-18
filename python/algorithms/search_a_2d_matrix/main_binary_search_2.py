#!/usr/bin/env python3

#binary search as if it were a 1D array

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        left = 0
        right = (height * width) - 1
        while left <= right:
            mid = (left + right) // 2
            row ,col = mid // width, mid % width
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))