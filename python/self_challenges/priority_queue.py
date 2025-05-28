# Insert and Pop O(logn). Peek O(1)
# Basically storing things as a binary tree underneath
# Not guaranteed to be fully sorted but guaranteed that parents always less than children
# Thus root is always min
class MinPriorityQueue:
    def __init__(self) -> None:
        self.heap = []
    
    # O(log n) time for sift up, O(1) space
    def insert(self, num: int) -> None:
        self.heap.append(num)

        # sift up from end of heap (where the new number is)
        # (swap it with as many parents as need be until it's smaller than all it's children)
        self._sift_up(len(self.heap) - 1)
    
    # O(1) time, O(1) space
    def peek(self) -> int:
        if not self.heap:
            return -1

        return self.heap[0]
    
    # O(log n) time for sift down, O(1) space
    def pop(self) -> int:
        if not self.heap:
            return -1
        
        # Get min value we will return
        min_val = self.heap[0]

        # Store what was the last element as we'll need to make sure it stays in array
        last = self.heap.pop()

        # Set first num to what was popped and sift down from start
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        
        return min_val

    # Implement binary tree where parent has left child 2*i + 1 and right child  2*i + 2
    # Sift a number up means make sure it's larger than it's parent 
    # Make swaps until that's the case
    # O(log n) time, O(1) space
    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            # If num is less than parent (shouldn't happen)
            # Swap them and sift up from parent
            if self.heap[idx] < self.heap[parent]:
                temp = self.heap[idx]
                self.heap[idx] = self.heap[parent]
                self.heap[parent] = temp
                idx = parent
            # Else we have our balanced tree
            else:
                break

    # Sift a number down means make sure a number is larger than it's children
    # Make swaps until that's the case
    # O(log n) time, O(1) space
    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            # Get left and right child indexes
            left = (2 * idx) + 1
            right = (2 * idx) + 2
            
            # Parent should be smallest
            smallest = idx
            # Left is smaller than parent
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Right is smaller than parent
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            # Smallest no longer equals parent so make swaps and re-do loop
            if smallest != idx:
                temp = self.heap[idx]
                self.heap[idx] = self.heap[smallest]
                self.heap[smallest] = temp
                idx = smallest
            # No swaps were needed so it's properly sifted so break out
            else:
                break

pq = MinPriorityQueue()
pq.insert(3)
pq.insert(0)
pq.insert(9)

assert(pq.peek() == 0)
popped = pq.pop()
assert(popped == 0), f"Popped wrong value. Popped {popped} should have been 0"
assert(pq.peek() == 3)