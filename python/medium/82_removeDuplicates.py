from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        placeHolderHead = ListNode(0, head)

        # predecessor = the last node before the sublist of duplicates
        predecessor = placeHolderHead
        
        while head:
            # if it's a beginning of duplicates sublist skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                predecessor.next = head.next 
            # otherwise, move predecessor
            else:
                predecessor = predecessor.next 
                
            # move forward
            head = head.next
            
        return placeHolderHead.next