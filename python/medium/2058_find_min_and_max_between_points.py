# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Traverse list once, keep first critical point as well as most recent
    # Find max and min distance
    # Time O(n)
    # Space O(1)
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        answer = [-1, -1]

        if not head:
            return answer

        # Initialize minimum distance to the maximum possible value
        min_distance = float("inf")

        # Pointers to track the previous node, current node, and indices
        previous_node = head
        current_node = head.next
        current_index = 1
        previous_critical_index = 0
        first_critical_index = 0

        while current_node and current_node.next is not None:
            # Check if the current node is a local minima or maxima
            if (
                current_node.val < previous_node.val
                and current_node.val < current_node.next.val
            ) or (
                current_node.val > previous_node.val
                and current_node.val > current_node.next.val
            ):

                # First critical point found so just store index
                if previous_critical_index == 0:
                    previous_critical_index = current_index
                    first_critical_index = current_index
                # Already had a critical point so update min distance if relevant
                else:
                    min_distance = min(min_distance, current_index - previous_critical_index)
                    previous_critical_index = current_index

            # Move to the next node and update indices
            current_index += 1
            previous_node = current_node
            current_node = current_node.next

        # If at least two critical points were found
        if min_distance != float("inf"):
            max_distance = previous_critical_index - first_critical_index
            answer = [min_distance, max_distance]

        return answer
