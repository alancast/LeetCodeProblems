from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSNode:
    def __init__(self, depth=0, node=None):
        self.depth = depth
        self.node = node


class Solution:
    # DFS to get depth or right and left root
    # If they are same return root, otherwise recursively call it on deeper side
    # Time O(n) as we do dfs
    # Space O(n) as deque could reach that size
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.find_depth(root).node

    def find_depth(self, root: TreeNode) -> DFSNode:
        if not root:
            return DFSNode(0, None)

        left = self.find_depth(root.left)
        right = self.find_depth(root.right)

        if left.depth > right.depth:
            left.depth += 1
            return left
        if left.depth < right.depth:
            right.depth += 1
            return right
        
        return DFSNode(left.depth + 1, root)
