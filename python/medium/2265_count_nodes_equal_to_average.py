# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Post order traversal to get the sum and count of nodes in each subtree
    # Time O(n)
    # Space O(n)
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Start with none
        self.answer = 0

        # Returns the sum of the subtree of that node as well as how many nodes in subtree
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            # Base case, if we hit a leaf node, return 0 sum and 0 count
            if not node:
                return 0, 0

            # Post order traversal, left and right then top
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # See if this node has value equal to average, if so increase answer
            if total_sum // total_count == node.val:
                self.answer += 1

            return total_sum, total_count

        # Do traversal from root
        dfs(root)

        return self.answer
