from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self._construct_tree(preorder, postorder)

    # Helper function to construct the tree recursively
    # Time O(n) n calls to _construct_tree
    # Space O(n) purely from the callstack being called n times
    def _construct_tree(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        # Recursively construct the left subtree if the root is not the last of its subtree
        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)

        # Recursively construct the right subtree if the root is not the last of its subtree
        if root.val != postorder[self.post_index]:
            root.right = self._construct_tree(preorder, postorder)

        # Mark this node and its subtree as fully processed
        self.post_index += 1
        return root

    def constructFromPrePost_index_array(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        num_of_nodes = len(preorder)

        # Create the index list for `postorder`
        index_in_post_order = [0] * (num_of_nodes + 1)
        for index in range(num_of_nodes):
            # Store the index of the current element
            index_in_post_order[postorder[index]] = index

        return self._construct_tree_index_array(0, num_of_nodes - 1, 0, preorder, index_in_post_order)

    # Helper function to construct the tree recursively
    # Time O(n) n calls to _construct_tree
    # Space O(n) create a length n index array
    def _construct_tree_index_array(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        index_in_post_order: List[int],
    ) -> Optional[TreeNode]:
        # Base case: If there are no nodes to process, return None
        if pre_start > pre_end:
            return None

        # Base case: If only one node is left, return that node
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        # The left child root in preorder traversal (next element after root)
        left_root = preorder[pre_start + 1]

        # Calculate the number of nodes in the left subtree by searching in postorder
        num_of_nodes_in_left = index_in_post_order[left_root] - post_start + 1

        root = TreeNode(preorder[pre_start])

        # Recursively construct the left subtree
        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            index_in_post_order,
        )

        # Recursively construct the right subtree
        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            index_in_post_order,
        )

        return root

    def constructFromPrePost_recursion(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        num_of_nodes = len(preorder)
        return self._construct_tree_recursion(0, num_of_nodes - 1, 0, preorder, postorder)

    # Helper function to construct the tree recursively
    # Time O(n^2) n calls to _construct_tree all of them linear traversal of list (O(n))
    # Space O(n) purely due to call stack being n levels deep
    def _construct_tree_recursion(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        postorder: List[int],
    ) -> Optional[TreeNode]:
        # Base case: If there are no nodes to process, return None
        if pre_start > pre_end:
            return None

        # Base case: If only one node is left, return that node
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        # The left child root in preorder traversal (next element after root)
        left_root = preorder[pre_start + 1]

        # Calculate the number of nodes in the left subtree by searching in postorder
        num_of_nodes_in_left = 1
        while postorder[post_start + num_of_nodes_in_left - 1] != left_root:
            num_of_nodes_in_left += 1

        root = TreeNode(preorder[pre_start])

        # Recursively construct the left subtree
        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            postorder,
        )

        # Recursively construct the right subtree
        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            postorder,
        )

        return root