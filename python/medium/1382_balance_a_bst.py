import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Use rotations to balance the binary tree
    # Use the Day Stout Warren algorithm
    # Time O(n)
    # Space O(1) due to recursion stack (otherwise O(1))
    def balanceBST_rotations(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Step 1: Create the backbone (vine)
        # Temporary dummy node
        vine_head = TreeNode(0)
        vine_head.right = root
        current = vine_head
        while current.right:
            if current.right.left:
                self._right_rotate(current, current.right)
            else:
                current = current.right

        # Step 2: Count the nodes
        node_count = 0
        current = vine_head.right
        while current:
            node_count += 1
            current = current.right

        # Step 3: Create a balanced BST
        m = 2 ** math.floor(math.log2(node_count + 1)) - 1
        self._make_rotations(vine_head, node_count - m)
        while m > 1:
            m //= 2
            self._make_rotations(vine_head, m)

        balanced_root = vine_head.right
        # Delete the temporary dummy node
        vine_head = None
        return balanced_root

    # Function to perform a right rotation
    def _right_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.left
        if tmp:
            node.left = tmp.right
            tmp.right = node
            parent.right = tmp

    # Function to perform a left rotation
    def _left_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.right
        if tmp:
            node.right = tmp.left
            tmp.left = node
            parent.right = tmp

    # Function to perform a series of left rotations to balance the vine
    def _make_rotations(self, vine_head: TreeNode, count: int):
        current = vine_head
        for _ in range(count):
            if current.right is None:
                break
            tmp = current.right
            self._left_rotate(current, tmp)
            current = current.right

    # Traverse tree in order to create sorted array
    # Then create tree from array
    # Time O(n) as we go over all nodes once then whole array once
    # Space O(n) for array
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        # Create a list to store the inorder traversal of the BST
        inorder = []
        self._inorder_traversal(root, inorder)

        # Construct and return the balanced BST
        return self._create_balanced_bst(inorder, 0, len(inorder) - 1)

    def _inorder_traversal(self, root: TreeNode | None, inorder: list):
        # Perform an inorder traversal to store the elements in sorted order
        if not root:
            return

        self._inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self._inorder_traversal(root.right, inorder)

    def _create_balanced_bst(self, inorder: list, start: int, end: int) -> TreeNode | None:
        # Base case: if the start index is greater than the end index, return None
        if start > end:
            return None

        # Find the middle element of the current range
        mid = start + (end - start) // 2

        # Recursively construct the left and right subtrees
        left_subtree = self._create_balanced_bst(inorder, start, mid - 1)
        right_subtree = self._create_balanced_bst(inorder, mid + 1, end)

        # Create a new node with the middle element and attach the subtrees
        return TreeNode(inorder[mid], left_subtree, right_subtree)
