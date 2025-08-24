from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Do an in order (left, parent, right) traversal of the tree
    # which by definition is sorted and just keep a deque
    # of size k with the k closest values
    # Time O(n) as each node is visited just once
    # Space O(n + k) n for call stack, k for deque
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # Do in order traversal and add k closest to queue
        def in_order(node: TreeNode, queue: deque) -> None:
            if not node:
                return
            
            # Check smaller child
            in_order(node.left, queue)

            # Process this node
            node_val = node.val
            # Always add onto end of deque
            queue.append(node_val)

            # See if queue is too big and needs popped, and see from what side to pop
            if len(queue) > k:
                distance = abs(node_val - target)
                left_distance = abs(queue[0] - target)

                # If the low side is closer than the high side pop the high
                # Also return as all future values will also be too high
                if distance > left_distance:
                    queue.pop()
                    return
                else:
                    queue.popleft()

            # Process right child
            in_order(node.right, queue)
            
        answer = deque()
        in_order(root, answer)

        return list(answer)
