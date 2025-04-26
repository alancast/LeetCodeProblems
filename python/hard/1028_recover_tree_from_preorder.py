from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def __init__(self):
        self.index = 0

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self._preorder_builder_list(traversal)
    
    # Basically same as stack, just no popping
    # Time O(n^2) worst case
    # Space O(n) depth of stack
    def _preorder_builder_list(self, traversal: str) -> Optional[TreeNode]:
        index = 0
        n = len(traversal)

        nodes = []
        while index < n:
            # Count the number of dashes to get depth
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Get the value
            value = 0
            while index < n and traversal[index].isdigit():
                value = (value * 10) + int(traversal[index])
                index += 1

            node = TreeNode(value)

            # Put node at right depth entry
            if depth < len(nodes):
                nodes[depth] = node
            else:
                nodes.append(node)

            # Attach node to parent
            if depth > 0:                
                if nodes[depth-1].left is None:
                    nodes[depth-1].left = node
                else:
                    nodes[depth-1].right = node

        return nodes[0]

    # Time O(n^2) worst case
    # Space O(n) depth of stack
    def _preorder_builder_stack(self, traversal: str) -> Optional[TreeNode]:
        index = 0
        n = len(traversal)

        nodes = []
        while index < n:
            # Count the number of dashes to get depth
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Get the value
            value = 0
            while index < n and traversal[index].isdigit():
                value = (value * 10) + int(traversal[index])
                index += 1

            node = TreeNode(value)

            # Adjust the stack to the correct depth
            while len(nodes) > depth:
                nodes.pop()

            # Attach node to parent
            if nodes:
                if nodes[-1].left is None:
                    nodes[-1].left = node
                else:
                    nodes[-1].right = node

            nodes.append(node)

        return nodes[0]
        
    # Time O(n^2) worst case completely skewed tree
    # Space O(n) recursion stack
    def _recursive_preorder_helper(self, traversal: str, depth: int) -> Optional[TreeNode]:
        # Reached end of traversal
        if self.index > len(traversal):
            return None
        
        # Figure out depth
        dash_count = 0
        while self.index < len(traversal) and traversal[self.index + dash_count] == "-":
            dash_count += 1

        # If dash_count doesn't equal depth it's a child of a different node
        if dash_count != depth:
            return None
        
        self.index += dash_count

        # Get value
        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = (value * 10) + int(traversal[self.index])
            self.index += 1

        node = TreeNode(value)

        node.left = self._recursive_preorder_helper(traversal, depth + 1)
        node.right = self._recursive_preorder_helper(traversal, depth + 1)

        return node
