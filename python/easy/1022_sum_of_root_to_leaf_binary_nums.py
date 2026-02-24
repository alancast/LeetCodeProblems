from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Do breadth first search and double num, then sum when no children
    # Time O(n)
    # Space O(logn) for queue
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        answer = 0
        queue = deque([(root, root.val)])
        while queue:
            node, num = queue.popleft()

            # If there are no children this is a leaf node
            if not node.left and not node.right:
                answer += num
                continue

            if node.left:
                queue.append((node.left, (num*2) + node.left.val))
            if node.right:
                queue.append((node.right, (num*2) + node.right.val))

        return answer
