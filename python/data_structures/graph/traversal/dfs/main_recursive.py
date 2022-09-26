#!/usr/bin/env python3

def dfs_recursive(graph, node, seen):
    seen[node] = True
    for neighbor in graph[node]:
        if not neighbor in seen:
            dfs_recursive(graph, neighbor, seen)