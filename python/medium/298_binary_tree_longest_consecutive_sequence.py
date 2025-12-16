from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Just recurse down left and right (can not use parent)
    # Time O(n)
    # Space O(n) for deque
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # DFS is in order traversal
        def dfs(node: Optional[TreeNode], prev_val: float, cur_max: int):
            if not node:
                return cur_max

            # See if this extends the streak
            if node.val == prev_val + 1:
                new_max = cur_max + 1
            else:
                new_max = 1

            # Return max of this, or left or right
            return max(cur_max, dfs(node.left, node.val, new_max), dfs(node.right, node.val, new_max))

        return dfs(root, float('-inf'), 0)
