# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head

        # find size of list and make a cycle pointing last one to head
        count = 1
        oldTail = head
        while oldTail.next:
            oldTail = oldTail.next
            count += 1

        # Create cycle
        oldTail.next = head

        # Break link where end should be and return new head
        index = (count - (k % count) - 1)
        newTail = head
        for _ in range(index):
            newTail = newTail.next # type: ignore

        newHead = newTail.next # type: ignore
        newTail.next = None # type: ignore

        return newHead
