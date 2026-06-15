# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Have one go two at a time and one go one
    # Once fast reaches end we know slow is in the middle
    # So just skip the middle one and return head
    # Time O(n)
    # Space O(1)
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None

        fast = head.next.next
        slow = head

        # Get fast to the end and move slow along
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # type: ignore

        # Slow is now at middle, so skip it
        slow.next = slow.next.next # type: ignore

        return head
