from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    answer_potential: Optional[TreeNode] = None

    # Time O(n) as each node could be visited once and does O(1) operations
    # Space O(1) as all we store is root
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor

    # Time O(n) as each node could be visited once and does O(1) operations
    # Space O(n) as tree could be a line so recursive call stack could be O(n)
    def inorderSuccessor_recursive(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        # We have a potential successor (but maybe not the smallest one)
        if root.val > p.val:
            # Is this successor smaller than the previous one
            if self.answer_potential and root.val < self.answer_potential.val:
                self.answer_potential = root
            # Do we not have any answer potential yet
            elif not self.answer_potential:
                self.answer_potential = root

        self.inorderSuccessor(root.left, p)
        self.inorderSuccessor(root.right, p)

        return self.answer_potential