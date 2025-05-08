from typing import List
import math


# Use a fenwick tree
# Don't fully understand this one. The square root buckets implementation is better
class FenwickTree:
    tree: List[int]

    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index = index & (index - 1)

        return result

    def insert(self, index, value):
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index


class MRUQueue:
    values: List[int]
    tree: FenwickTree
    size: int

    def __init__(self, n):
        self.size = n
        self.tree = FenwickTree(n + 2000)
        self.values = [0] * (n + 2000)
        for i in range(n):
            self.tree.insert(i, 1)
            self.values[i] = i + 1

    def fetch(self, k):
        low = 0
        high = self.size
        while low < high:
            mid = (low + high) >> 1
            if self.tree.sum(mid) < k:
                low = mid + 1
            else:
                high = mid

        self.tree.insert(low - 1, -1)
        self.tree.insert(self.size, 1)
        self.values[self.size] = self.values[low - 1]
        self.size += 1

        return self.values[low - 1]


class MRUQueueBuckets:
    buckets: List[List[int]]
    index: List[int]
    BUCKET_SIZE: int
    TOTAL_ELEMENTS: int

    def __init__(self, n: int):
        self.TOTAL_ELEMENTS = n
        self.BUCKET_SIZE = math.isqrt(n)
        self.buckets = []
        self.index = []

        for number in range(1, n + 1):
            bucket_index = (number - 1) // self.BUCKET_SIZE

            # See if final bucket is full so we need a new bucket
            if bucket_index == len(self.buckets):
                self.buckets.append([])
                self.index.append(number)

            self.buckets[-1].append(number)
        

    # Time O(sqrt n) as it's sqrt n to find bucket and sqrt n within
    def fetch(self, k: int) -> int:
        # Find bucket index for k
        bucket_index = self._upper_bound(self.index, k) - 1

        # Fetch the element then remove it from this list
        element = self.buckets[bucket_index][k - self.index[bucket_index]]
        del self.buckets[bucket_index][k - self.index[bucket_index]]

        # Move all subsequent bucket indexes down one now that this element is in the back
        for i in range(bucket_index + 1, len(self.index)):
            self.index[i] -= 1

        # See if final bucket is full and thus we need to append a new bucket
        if len(self.buckets[-1]) >= self.BUCKET_SIZE:
            self.buckets.append([])
            self.index.append(self.TOTAL_ELEMENTS)
        self.buckets[-1].append(element)

        # If the new bucket is empty now delete that bucket
        if len(self.buckets[bucket_index]) == 0:
            del self.buckets[bucket_index]
            del self.index[bucket_index]

        return element
    
    # Time O(sqrt n) as it's binary search
    def _upper_bound(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left


class MRUQueueBruteForce:
    queue: List[int]

    def __init__(self, n: int):
        self.queue = [i for i in range(n+1)]
        

    # Time O(n) as we move every element in the array each time
    def fetch(self, k: int) -> int:
        element = self.queue[k]
        self.queue.pop(k)
        self.queue.append(element)

        return element


# Your MRUQueue object will be instantiated and called as such:
obj = MRUQueue(10)
param_1 = obj.fetch(3)