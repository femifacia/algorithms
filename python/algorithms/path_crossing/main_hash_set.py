class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set([(0,0)])
        moove = {"N" : (0,1), "E" : (1,0), "W" : (-1,0), "S" :(0,-1)}
        x,y = (0,0)
        for i in path:
            x += moove[i][0]
            y += moove[i][1]
            if (x,y) in seen:
                return True
            seen.add((x,y))
        return False