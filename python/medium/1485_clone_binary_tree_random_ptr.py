# Definition for Node.
from collections import deque


# Definition of node class
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Useless class because problem needs answer in this type
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def __init__(self):
        # Hashmap to map old tree's nodes with new tree's nodes.
        self.seen: dict = {None: None}

    # Function to traverse on the sub graph of 'root'.
    def bfs(self, root: Node | None) -> NodeCopy | None:
        if not root:
            return None

        queue = deque()
        # Push root in queue, mark it as seen and store its respective new node.
        queue.append(root)
        self.seen[root] = NodeCopy(root.val)

        # Go through BFS
        while queue:
            old_node = queue.popleft()
            new_node = self.seen[old_node]

            # Traverse on left, right and random edges one-by-one, if nodes exist and,
            # not already seen then we push it in queue, create a copy and attach it to new node.
            if old_node.left:
                if old_node.left not in self.seen:
                    queue.append(old_node.left)
                    self.seen[old_node.left] = NodeCopy(old_node.left.val)
                new_node.left = self.seen[old_node.left]

            if old_node.right:
                if old_node.right not in self.seen:
                    queue.append(old_node.right)
                    self.seen[old_node.right] = NodeCopy(old_node.right.val)
                new_node.right = self.seen[old_node.right]

            if old_node.random:
                if old_node.random not in self.seen:
                    queue.append(old_node.random)
                    self.seen[old_node.random] = NodeCopy(old_node.random.val)
                new_node.random = self.seen[old_node.random]

        return self.seen[root]

    # Do BFS on the tree and copy
    # Time O(n)
    # Space O(n)
    def copyRandomBinaryTree(self, root: Node | None) -> NodeCopy | None:
        # Traverse on each node of the given tree.
        return self.bfs(root)
