from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Class to help find biggest BST subtree
# Stores min node in range and max node in range as well as biggest BST size underneath
class TreeScanHelper:
    def __init__(self, min_node: int, max_node: int, max_size: int):
        self.min_node = min_node
        self.max_node = max_node
        self.max_size = max_size


class Solution:
    # Time O(n) as all tree nodes are traversed once and do O(1) ops
    # Space O(n) as call stack could be all nodes if tree is straight line
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self._largest_bst_subtree_helper(root).max_size
    
    # Recurses through all subtrees. Stores min and max value of left and right
    # As well of size of largest BST
    def _largest_bst_subtree_helper(self, root: Optional[TreeNode]) -> TreeScanHelper:
        if not root:
            # Invert min and max
            return TreeScanHelper(float('inf'), float('-inf'), 0)
        
        left = self._largest_bst_subtree_helper(root.left)
        right = self._largest_bst_subtree_helper(root.right)
        
        # See if valid bst
        if left.max_node >= root.val or right.min_node <= root.val:
            # not a valid bst but return size of biggest one under it
            return TreeScanHelper(float('-inf'), float('inf'), max(left.max_size, right.max_size))
        
        # Need to include root in these min and maxes because there might not be a 
        # left or right subtree, so the root is the min or max
        return TreeScanHelper(
            min(root.val, left.min_node),
            max(root.val, right.max_node),
            left.max_size + right.max_size + 1
        )