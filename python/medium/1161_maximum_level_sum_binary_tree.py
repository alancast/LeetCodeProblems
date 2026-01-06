from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # A breadth first search computing sum on each level
    # Time O(n) as each node is seen once
    # Space O(logn) as queue is log of tree
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        current_level_sum = max_sum = root.val # type: ignore
        max_level = 1
        current_level = 0

        queue = deque()
        queue.append((root, 1))

        # BFS to process nodes
        while queue:
            node, level = queue.popleft()

            # We are starting a new level
            if level != current_level:
                # See if last level was new max
                if current_level_sum > max_sum:
                    max_sum = current_level_sum
                    max_level = current_level

                # Reset to new level
                current_level = level
                current_level_sum = 0

            current_level_sum += node.val

            # Add children nodes to queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # See if final level was max
        if current_level_sum > max_sum:
            max_sum = current_level_sum
            max_level = current_level

        return max_level
