from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Traverse tree one and create a set of all the values
    # Then traverse second tree and search for target
    # Time O(n)
    # Space O(n)
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # Traverse tree one and create set of it
        values_one = set()
        bfs_deque = deque()
        bfs_deque.append(root1)
        while bfs_deque:
            node = bfs_deque.popleft()
            values_one.add(node.val)
            if node.left:
                bfs_deque.append(node.left)
            if node.right:
                bfs_deque.append(node.right)
        
        # Traverse tree two and see if it's possible to get sum
        bfs_deque.append(root2)
        while bfs_deque:
            node = bfs_deque.popleft()
            need = target - node.val
            if need in values_one:
                return True

            if node.left:
                bfs_deque.append(node.left)
            if node.right:
                bfs_deque.append(node.right)

        # If we traversed the whole tree and didn't find anything then not possible
        return False
