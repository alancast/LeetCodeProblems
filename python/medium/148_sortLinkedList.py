# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Using merge sort. Slower than other way, but less memory
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        # This makes sure to split the list into halves (since fast is moving twice as fast)
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # type: ignore
        start = slow.next # type: ignore
        slow.next = None # type: ignore

        # recurse on left list and right list
        left = self.sortList(head)
        right = self.sortList(start)

        # Merge the lists together
        return self.merge(left, right)


    def merge(self, left: ListNode | None, right: ListNode | None) -> ListNode | None:
        if not left or not right:
            return left or right

        # Merge the lists
        dummy = p = ListNode(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        # Take care of remaining lists
        p.next = left or right

        # return head
        return dummy.next

    # Insert values into a dictionary, then sort the dictionary and point to nodes
    def sortListMaps(self, head: ListNode | None) -> ListNode | None:
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
