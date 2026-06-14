# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # If space is not needed just push to a list and add i and -i
    # If space is at a premium, can reverse second half of list in place
    # And keep pointer to first and last and add from there
    # Time O(n)
    # Space O(1)
    def pairSum(self, head: ListNode | None) -> int:
        # Create a slow and fast to find middle of even length list
        slow = head
        fast = head
        answer = 0

        # Get middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # type: ignore

        # Reverse second half of the linked list
        # We know slow is at midpoint
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # By now we know prev is at the last item in the list
        start = head
        while prev and start:
            # See if we have a new max pair
            answer = max(answer, start.val + prev.val)
            prev = prev.next
            start = start.next

        return answer
