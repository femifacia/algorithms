#!/usr/bin/env python3
class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        node1_to  = edges[node1]
        node2_to = edges[node2]
        if (node1_to == node2_to):
            return (2)
        