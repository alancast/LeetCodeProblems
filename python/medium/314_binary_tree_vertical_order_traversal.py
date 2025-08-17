from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS use a queue to keep column number
    # Use a dictionary of column number to list. Top to bottom ordering
    # is guaranteed because BFS. left to right ordering is done by
    # Appending left child before right children
    # Time O(n) as each node is processed once with O(1) operations
    # Space O(n) as we keep full dictionary of same size as tree
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        leftmost = rightmost = 0

        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
        column_lists = defaultdict(list)

        # Create the top to bottom lists of all the verticals
        while queue:
            node, vertical = queue.popleft()
            leftmost = min(leftmost, vertical)
            rightmost = max(rightmost, vertical)

            column_lists[vertical].append(node.val)

            # Add left child to queue
            if node.left:
                queue.append((node.left, vertical - 1))

            # Add right child to queue
            if node.right:
                queue.append((node.right, vertical + 1))

        # Turn the top to bottom lists into an array
        return [column_lists[x] for x in range(leftmost, rightmost + 1)]
