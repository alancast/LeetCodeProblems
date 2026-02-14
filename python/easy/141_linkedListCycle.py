# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time complexity optimized.
    # O(n) extra space, min possible runtime (but still O(n))
    def hasCycle(self, head: ListNode | None) -> bool:
        nodes = set()

        while head:
            if head in nodes:
                return True

            nodes.add(head)
            head = head.next

        return False

    # Space complexity optimized.
    # O(1) extra space, larger than O(n) time if cycle
    def hasCycleMinSpace(self, head: ListNode | None) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head

        while fast and fast.next and slow:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
