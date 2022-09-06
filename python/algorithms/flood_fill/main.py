#!/usr/bin/env python3

class Solution:

    def fill(self, image, sr, sc, color, x, y ,dic):
        if ((sr, sc) in dic):
            return
        dic[(sr,sc)] = 1
        if (sr + 1< y and image[sr + 1][sc] == image[sr][sc]):
            self.fill(image, sr + 1, sc, color, x, y, dic)
        if (sr - 1 >= 0 and image[sr - 1][sc] == image[sr][sc]):
            self.fill(image, sr - 1, sc, color, x, y, dic)
        if (sc + 1 < x and image[sr][sc + 1] == image[sr][sc]):
            self.fill(image, sr, sc + 1, color, x, y, dic)
        if (sc - 1 >= 0 and image[sr][sc - 1] == image[sr][sc]):
            self.fill(image, sr, sc - 1, color, x, y, dic)
        image[sr][sc] = color

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        x = len(image[0])
        y = len(image)
        dic = {}
        self.fill(image, sr, sc, color, x, y, dic)
        return image
    
sol = Solution()
print("before")
arr = [[0]]
for i in arr:
    print(i)
sol.floodFill(arr,0, 0, 2)
print("after")
for i in arr:
    print(i)