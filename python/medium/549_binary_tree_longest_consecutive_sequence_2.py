from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Single traversal of tree
    # Time O(n) as each node in tree is visited once
    # Space O(n) for call stack
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        # Returns an array in form [incrementing, decrementing]
        # Which represent the longest incrementing and decrementing
        # path beneath this node. Including itself
        def find_longest_path(root: Optional[TreeNode]) -> List[int]:
            nonlocal longest_path

            # Not a real node, so 0,0
            if not root:
                return [0, 0]

            # Count your own node, so always starts at 1
            incrementing = decrementing = 1

            # Recurse on left and right subtree
            if root.left:
                left = find_longest_path(root.left)

                # See if this node is one greater or less than children
                # And thus continues path
                if (root.val == root.left.val + 1):
                    decrementing = left[1] + 1
                elif (root.val == root.left.val - 1):
                    incrementing = left[0] + 1

            if root.right:
                right = find_longest_path(root.right)

                # See if this node is one greater or less than children
                # And thus continues path
                if (root.val == root.right.val + 1):
                    decrementing = max(decrementing, right[1] + 1)
                elif (root.val == root.right.val - 1):
                    incrementing = max(incrementing, right[0] + 1)

            longest_path = max(longest_path, decrementing + incrementing - 1)
            return [incrementing, decrementing]

        # This is modified in the longest path recursive function
        longest_path = 0
        find_longest_path(root)

        return longest_path
