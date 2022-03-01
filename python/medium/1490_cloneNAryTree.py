# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def cloneTree(self, root: Node) -> Node:
        if not root:
            return root

        new_root = Node(root.val)
        # Starting point to kick off the BFS visits.
        queue = deque([(root, new_root)])

        while queue:
            old_node, new_node = queue.popleft()

            for child_node in old_node.children:
                new_child_node = Node(child_node.val)
                new_node.children.append(new_child_node)
                queue.append((child_node, new_child_node))

        return new_root