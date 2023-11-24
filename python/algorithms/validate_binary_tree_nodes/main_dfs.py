#!/usr/bin/env python3

# Not finished

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        seen = set()
        allNodes = set(range(n))
        start = 0
        parents = [-1] * n
        to_see = [0]
        heads = set()
        #print(not(seen ^ allNodes))
        while  (seen ^ allNodes):
#            print(seen)
            to_see = [(seen ^ allNodes).pop()]
            if to_see[0] in seen:
                return False
            seen.add(to_see[0])
            heads.add(to_see[0])
            while (to_see):
                current = to_see.pop()
#                print(current)
                left = leftChild[current]
                right = rightChild[current]
                if (left in seen and parents[left] != -1) or (right in seen and parents[right] != -1):
                    print(parents, current, left, right, seen)
                    return False
                if left >= 0:
                    seen.add(left)
                    if parents[left] == -1:
                        to_see.append(left)
                    parents[left] = current
                if right >= 0:
                    seen.add(right)
                    if parents[right] == -1:
                        to_see.append(right)
                    parents[right] = current
#                print(left,right)
        if parents.count(-1) > 1:
#            print(parents)
            return False
        return True

sol = Solution()
n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]
n = 2
leftChild = [1,0]
rightChild = [-1,-1]
n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,3,-1,-1]
n = 6
leftChild = [1,-1,-1,4,-1,-1]
rightChild = [2,-1,-1,5,-1,-1]
n = 4
leftChild = [3,-1,1,-1]
rightChild = [-1,-1,0,-1]
print(sol.validateBinaryTreeNodes(n, leftChild, rightChild))