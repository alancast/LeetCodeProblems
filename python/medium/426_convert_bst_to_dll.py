from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time O(n) as each node is processed once
    # Space O(n) for recursive stack
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return

        # Helper to do inorder traversal
        def in_order_helper(node: Optional[Node]):
            if not node:
                return
            
            # left
            in_order_helper(node.left)

            nonlocal tail, head
            # node
            if tail:
                tail.right = node
                node.left = tail
            else:
                # Keep first node as head (only set once)
                head = node

            tail = node

            # right
            in_order_helper(node.right)

        head: Optional[Node] = None
        tail: Optional[Node] = None

        in_order_helper(root)

        # Close off doubly linked list
        head.left = tail
        tail.right = head

        return head