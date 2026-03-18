# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        placeHolderHead = ListNode(0, head)

        # predecessor = the last node before the sublist of duplicates
        predecessor = placeHolderHead

        while head:
            # if it's a beginning of duplicates sublist skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val: # type: ignore
                    head = head.next # type: ignore
                # skip all duplicates
                predecessor.next = head.next # type: ignore
            # otherwise, move predecessor
            else:
                predecessor = predecessor.next # type: ignore

            # move forward
            head = head.next # type: ignore

        return placeHolderHead.next
