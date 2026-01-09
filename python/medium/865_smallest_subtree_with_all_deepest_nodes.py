from typing import Optional
from typing import NamedTuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Result(NamedTuple):
    # The lowest node which is a parent to all the deepest heights
    node: Optional[TreeNode]
    # The height of the node
    height: int


class Solution:
    # Recurse down subtree and find height of left and right
    # If they are the same height, then this could be the answer
    # If they are a different height, the answer is whichever one is taller
    # Time O(n)
    # Space O(n)
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Result:
            # Return the result of the subtree at this node.
            if not node:
                return Result(None, 0)

            # Recurse down left and right
            L = dfs(node.left)
            R = dfs(node.right)

            # If one subtree is deeper than the other this node isn't answer
            if L.height > R.height:
                return Result(L.node, L.height + 1)
            if L.height < R.height:
                return Result(R.node, R.height + 1)

            # They are the same height, so this is the node we want
            return Result(node, L.height + 1)

        return dfs(root).node
