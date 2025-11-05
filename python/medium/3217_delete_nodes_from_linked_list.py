from typing import List, Optional


# Definition for singly-linheaded list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Create a set of all the nums
    # Go over list and skip anything in nums
    # Time O(n)
    # Space O(n)
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create num_set
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        # Go over all items in list and skip ones in num_set
        # Set head first
        while head and head.val in num_set:
            head = head.next
        
        # Iterate after head
        temp_head = head
        while temp_head.next:
            if temp_head.next.val in num_set:
                temp_head.next = temp_head.next.next
            else:
                temp_head = temp_head.next

        return head
