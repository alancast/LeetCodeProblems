from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        preHead = ListNode()
        head = preHead
        carriedValue = 0
        while l1 and l2:
            nextVal = (l1.val + l2.val + carriedValue) % 10
            carriedValue =  (l1.val + l2.val + carriedValue) // 10
            head.next = ListNode(nextVal)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        # If one list is longer than the other this will be true
        while l1:
            nextVal = (l1.val + carriedValue) % 10
            carriedValue =  (l1.val + carriedValue) // 10
            head.next = ListNode(nextVal)
            head = head.next
            l1 = l1.next
        while l2:
            nextVal = (l2.val + carriedValue) % 10
            carriedValue =  (l2.val + carriedValue) // 10
            head.next = ListNode(nextVal)
            head = head.next
            l2 = l2.next
        
        # In case the final digit is a carried over 1
        if carriedValue:
            head.next = ListNode(carriedValue)

        return preHead.next
