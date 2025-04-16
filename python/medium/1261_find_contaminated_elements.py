# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# So many ways to do this
# Can lazy load and do nothing in init
# Could compute whole tree in init and store all values in a hash map
# In which case init is expensive but find is always O(1)
# But the class takes up a lot of memory
# Could do nothing on init and always compute at find where every find call is log(n)
# This implementation will be compute whole tree on init and create hash map
class FindElements:
    seen: set[int]

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs_build_tree(root, 0)
        
    def find(self, target: int) -> bool:
        return target in self.seen
    
    def dfs_build_tree(self, current_node, current_value):
        if current_node is None:
            return
        # visit current node by adding its value to seen
        self.seen.add(current_value)
        self.dfs_build_tree(current_node.left, current_value * 2 + 1)
        self.dfs_build_tree(current_node.right, current_value * 2 + 2)
        
    def bfs_build_tree(self, root: TreeNode) -> None:
        root.val = 0
        queue = [root]

        while queue:
            node: TreeNode = queue.pop()
            self.seen.add(node.val)
            if node.left:
                node.left.val = (2 * node.val) + 1
                queue.append(node.left)
            if node.right:
                node.right.val = (2 * node.val) + 2
                queue.append(node.right)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)