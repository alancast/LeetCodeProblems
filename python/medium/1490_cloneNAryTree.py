from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    # BFS deep copy
    # Time O(n)
    # Space O(n)
    def cloneTree(self, root: Node) -> Node:
        if not root:
            return root

        new_root = Node(root.val)
        # Starting point to kick off the BFS visits.
        queue = deque([(root, new_root)])

        # Go over all nodes and just copy them
        while queue:
            old_node, new_node = queue.popleft()

            # For every old child create a new child and add to queue
            for child_node in old_node.children:
                new_child_node = Node(child_node.val)
                new_node.children.append(new_child_node)
                queue.append((child_node, new_child_node))

        return new_root
