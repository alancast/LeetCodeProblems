# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    MAX_HEIGHT_DIFFERENCE = 2

    # DFS to see if nodes are balanced
    # Time O(n) go over each node once
    # Space O(n) for call stack
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.balanced = True

        def dfs(node):
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                self.balanced = False

            return max(left_height, right_height) + 1

        dfs(root)
        return self.balanced

    # Go from root and see if each smaller one ins balanced
    # Time O(n) each node processed once
    # Space O(n) for call stack
    def isBalanced_complicated(self, root: TreeNode | None) -> bool:
        return self._isBalancedHelper(root)[0]

    # Returns if tree is balanced as well as height of tree
    def _isBalancedHelper(self, root: TreeNode | None) -> tuple[bool, int]:
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self._isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0

        rightIsBalanced, rightHeight = self._isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced using their height
        is_balanced = abs(leftHeight - rightHeight) < self.MAX_HEIGHT_DIFFERENCE
        return (is_balanced, 1 + max(leftHeight, rightHeight))
