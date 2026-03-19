# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time O(n)
    # Space O(n) for sums seen list
    def checkEqualTree(self, root: TreeNode | None) -> bool:
        if not root:
            return False

        # Can't use a set because things can get wonky if tree sum is 0
        self.sums_seen = []
        tree_sum = self._get_tree_sum(root)
        if tree_sum % 2 == 1:
            return False

        target_sum = tree_sum // 2

        # Make sure that the sum appears somewhere in the tree other than at the root
        # Because if only at the root then we can't cut into two equal trees
        self.sums_seen.pop()

        return any(sum == target_sum for sum in self.sums_seen)

    # Time O(n) go over each node once
    # Space O(logn) call stack
    def _get_tree_sum(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        sum = root.val
        sum += self._get_tree_sum(root.left)
        sum += self._get_tree_sum(root.right)

        self.sums_seen.append(sum)

        return sum
