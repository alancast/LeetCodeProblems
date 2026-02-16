# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time O(len(list))
    # Space O(1)
    def deleteNodes(self, head: ListNode | None, m: int, n: int) -> ListNode | None:
        pre_head = ListNode(next=head)

        # Go through list until it's done
        kept_count = 1
        while head:
            # Keeping
            if kept_count < m:
                kept_count += 1
            # Time to skip some
            else:
                skipped_count = 0
                while skipped_count < n and head.next:
                    head.next = head.next.next
                    skipped_count += 1

                kept_count = 1

            head = head.next

        return pre_head.next
