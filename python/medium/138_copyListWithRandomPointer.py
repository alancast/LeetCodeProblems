from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # O(N) time O(1) space by weaving list in
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
    
        return head_new

    # O(N) time and space
    def copyRandomListON(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        # Key: Old node. Value: New node
        visited = {}

        old_node = head
        # Creating the new head node.       
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node:
            # Populate new random node
            if old_node.random:
                if old_node.random not in visited:
                    visited[old_node.random] = Node(old_node.random.val, None, None)
                new_node.random = visited[old_node.random]
                
            # Populate new next node
            if old_node.next:
                if old_node.next not in visited:
                    visited[old_node.next] = Node(old_node.next.val, None, None)
                new_node.next = visited[old_node.next]

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return visited[head]
