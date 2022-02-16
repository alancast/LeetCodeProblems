# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nextHead = head.next

        previous = ListNode()
        swap1 = head
        swap2 = head.next
        while swap2:
            previous.next = swap2
            next_swap1 = swap2.next
            swap2.next = swap1
            swap1.next = next_swap1
            previous = swap1
            swap1 = next_swap1
            if not swap1:
                break
            swap2 = swap1.next

        return nextHead  

    def swapPairsRecurse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
              