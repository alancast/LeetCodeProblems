from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    MOD = 10**9 + 7

    # Do DFS over tree to find total tree sum
    # Each time you find a sum, add it to a set
    # Go over all sums at end and see what is max product
    # Time O(n) as each node is visited once
    # Space O(n) as recursive call stack as well as storage of sums
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = set()

        # Compute the total sum of a tree with this as the root node
        def tree_sum(root: Optional[TreeNode]) -> int:
            # If no node just return
            if not root:
                return 0

            # Find children tree sums
            left_sum = tree_sum(root.left)
            right_sum = tree_sum(root.right)

            # Compute total sum and add it to the sums list
            total_sum = left_sum + right_sum + root.val
            all_sums.add(total_sum)

            return total_sum

        total = tree_sum(root)
        answer = 0

        # Go over all sums and compute product they can produce
        for sum in all_sums:
            answer = max(answer, sum * (total - sum))   

        return answer % self.MOD
