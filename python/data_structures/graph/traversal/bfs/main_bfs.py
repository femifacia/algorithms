#!/usr/bin/env python3

from collections import deque


def bfs(graph, start=0):
    to_see = deque()
    dist = [float('inf')] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_see.appendleft(start)
    while (to_see):
        current = to_see.pop()
        for neighbor in graph[current]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[current] + 1
                prec[neighbor] = current
                to_see.appendleft(neighbor)
    return (dist, prec)