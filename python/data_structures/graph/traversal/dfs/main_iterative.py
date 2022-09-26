#!/usr/bin/env python3

def dfs_iterative(graph, start):
    to_see = [start]
    seen = {}
    while to_see:
        current_node = to_see.pop()
        seen[current_node] = True
        for neighbor in graph[current_node]:
            if not neighbor in seen:
                to_see.append(current_node)