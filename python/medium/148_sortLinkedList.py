# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Using merge sort. Slower than other way, but less memory
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # This makes sure to split the list into halves (since fast is moving twice as fast)
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None

        # recurse on left list and right list
        l, r = self.sortList(head), self.sortList(start)

        # Merge the lists together
        return self.merge(l, r)
        
        
    def merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        if not l or not r:
            return l or r
        
        # Merge the lists
        dummy = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        # Take care of remaining lists
        p.next = l or r

        # return head
        return dummy.next

    # Insert values into a dictionary, then sort the dictionary and point to nodes
    def sortListMaps(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nodesMap = {}
        while head:
            if head.val in nodesMap:
                nodesMap[head.val].append(head)
            else:
                nodesMap[head.val] = [head]
            head = head.next
        
        previousNode = ListNode()
        newHead = previousNode
        for _, nodes in sorted(nodesMap.items()):
            for node in nodes:
                previousNode.next = node
                previousNode = node
        
        previousNode.next = None
        
        return newHead.next