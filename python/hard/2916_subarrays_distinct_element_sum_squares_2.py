from collections import defaultdict


class BIT:
    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    def _lowbit(self, index: int) -> int:
        return index & -index

    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        index += 1
        if index < 0:
            raise ValueError("index must be a positive integer")

        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        index += 1
        index = min(index, self.size)

        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return res


class Solution:
    # Binary Tree
    # Time O(n log n)
    # Space O(n)
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        res = cur = 0
        bit = BIT(n + 10)
        seen = {}
        mod = 10**9 + 7

        for index, num in enumerate(nums):
            j = seen.get(num, -1) + 1
            cur += bit.query(j, index) * 2 + index - j + 1
            res += cur
            bit.add(j, index, 1)
            seen[num] = index

        return res % mod

test_cases = [
    [15, [1,2,1]],
    [3, [2,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.sumCounts(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
