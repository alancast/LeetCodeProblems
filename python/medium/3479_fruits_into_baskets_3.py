from math import sqrt
from typing import List


class SegTree:
    def __init__(self, baskets):
        # Number of baskets
        self.n = len(baskets)
        # Size of segment tree array (next power of 2 * 2)
        size = 2 << (self.n - 1).bit_length()
        # Segment tree to store max basket capacity in each segment
        self.seg = [0] * size
        # Build the segment tree from the baskets array
        self._build(baskets, 1, 0, self.n - 1)

    def _maintain(self, node):
        # Update the current node with the max value of its children
        self.seg[node] = max(self.seg[node * 2], self.seg[node * 2 + 1])

    def _build(self, baskets, node, left, right):
        # Recursively build the segment tree
        if left == right:
            # Leaf node: store basket capacity
            self.seg[node] = baskets[left]
            return

        mid = (left + right) // 2
        # Build left child
        self._build(baskets, node * 2, left, mid)
        # Build right child
        self._build(baskets, node * 2 + 1, mid + 1, right)
        # Maintain current node value
        self._maintain(node)

    def find_first_and_update(self, node, left, right, fruit_count):
        # Find the first basket with capacity >= fruit_count and set it as used
        if self.seg[node] < fruit_count:
            # No basket in this segment can hold fruit_count fruits
            return -1

        if left == right:
            # Found a basket, mark it as used (-1)
            self.seg[node] = -1
            return left

        mid = (left + right) // 2

        # Try to find in the left child
        index = self.find_first_and_update(node * 2, left, mid, fruit_count)
        if index == -1:
            # If not found, try right child
            index = self.find_first_and_update(node * 2 + 1, mid + 1, right, fruit_count)

        # Update current node after change
        self._maintain(node)

        return index


class Solution:
    # Perfect use of a segment tree
    # Create segment tree and use it to place fruits
    # Time O(nlogn) as segment tree update and binary search is logn
    # Space O(n) store full segment tree which is O(n)
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        tree = SegTree(baskets)

        answer = 0
        for fruit in fruits:
            # See first place this fruit can be placed
            # If nowhere, add it to the answer
            if tree.find_first_and_update(1, 0, n - 1, fruit) == -1:
                answer += 1

        return answer
    
    # Go over every fruit and for each one go over baskets groupings
    # Group buckets into sqrt(n) sizes and skip whole bucket if nothing is big enough
    # After using a basket set it's capacity to zero
    # Time O(n * sqrt(n)) as for every fruit we go through nested basket index
    # Space O(sqrt(n))
    def numOfUnplacedFruits_buckets(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        bucket_size = int(sqrt(n))

        # How many buckets isn't just bucket_size (take n=99 for example)
        buckets = (n + bucket_size - 1) // bucket_size

        # Create bucket maxes
        bucket_max = [0] * buckets
        for i in range(n):
            bucket_max[i//bucket_size] = max(bucket_max[i//bucket_size], baskets[i])

        answer = 0
        # Go over all fruits to see what basket they belong in
        for fruit_count in fruits:
            placed = False

            # Go over all baskets (bucket by bucket)
            for bucket in range(buckets):
                # Nothing in bucket is big enough
                if bucket_max[bucket] < fruit_count:
                    continue

                # Something in the bucket is big enough, so use it and update max
                bucket_max[bucket] = 0
                for i in range(bucket_size):
                    index = bucket * bucket_size + i

                    # We are placing the fruit in this bucket
                    if index < n and baskets[index] >= fruit_count and not placed:
                        baskets[index] = 0
                        placed = True

                    # Update the bucket max
                    if index < n:
                        bucket_max[bucket] = max(bucket_max[bucket], baskets[index])

                # Don't do other buckets since we have now done this one
                break

            # See if fruit couldn't be placed
            if not placed:
                answer += 1

        return answer
    
    # Go over every fruit and for each one go over baskets list in order
    # After using a basket set it's capacity to zero
    # Time O(n^2) as for every fruit we go through nested basket index
    # Space O(1)
    def numOfUnplacedFruits_brute_force(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        answer = 0
        # Go over all fruits to see what basket they belong in
        for fruit_count in fruits:
            placed = False

            # Go over all baskets
            for i in range(n):
                # Check if this capacity is big enough and use it
                basket_capacity = baskets[i]
                if fruit_count <= basket_capacity:
                    placed = True
                    baskets[i] = 0
                    break

            # See if fruit couldn't be placed
            if not placed:
                answer += 1

        return answer

test_cases = [
    [1, [4,2,5], [3,5,4]],
    [0, [3,6,1], [6,4,7]]
]
solution = Solution()
for expected, fruits, baskets in test_cases:
    actual = solution.numOfUnplacedFruits(fruits, baskets)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: fruits: {fruits}, baskets: {baskets}")

print("Ran all tests")