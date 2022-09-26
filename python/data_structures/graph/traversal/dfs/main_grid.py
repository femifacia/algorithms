#!/usr/bin/env python3

def dfs_grid_recursive(grid, i, j, mark="+", free="#"):
    height = len(grid)
    width = len(grid[0])
    to_see = [(i, j)]
    while to_see:
        i1, j1 = to_see.pop()
        for i2, j2 in [(i1 + 1, j1), (i1, j1 + 1), (i1, j1 - 1), (i1 -1, j1)]:
            if 0 <= i2 < height and 0 <= j2 < width and grid[i2][j2] == free:
                to_see.append((i2, j2))
                grid[i2][j2] = mark