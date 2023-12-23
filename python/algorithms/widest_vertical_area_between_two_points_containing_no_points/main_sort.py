class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x : x[0])
        ans = 0
        for i in range(len(points) - 1):
            ans = max(ans, points[i + 1][0] - points[i][0])
        return ans