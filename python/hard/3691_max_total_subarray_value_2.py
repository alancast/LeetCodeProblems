from heapq import heapify, heappop, heappush


class SegTree:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.max_val = [0] * (4 * self.n)
        self.min_val = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node: int, left: int, right: int, nums: list[int]):
        if left == right:
            self.max_val[node] = self.min_val[node] = nums[left]
            return

        mid = left + ((right - left) // 2)
        # Build left
        self.build(node * 2, left, mid, nums)
        # Build right
        self.build(node * 2 + 1, mid + 1, right, nums)
        self.max_val[node] = max(self.max_val[node * 2], self.max_val[node * 2 + 1])
        self.min_val[node] = min(self.min_val[node * 2], self.min_val[node * 2 + 1])

    def queryMax(self, node: int, left: int, right: int, ql: int, qr: int) -> int:
        if ql <= left and right <= qr:
            return self.max_val[node]

        mid = left + ((right - left) // 2)
        # Just a large neg number to set bounds
        answer = -(10**18)
        if ql <= mid:
            answer = max(answer, self.queryMax(node * 2, left, mid, ql, qr))
        if qr > mid:
            answer = max(answer, self.queryMax(node * 2 + 1, mid + 1, right, ql, qr))

        return answer

    def queryMin(self, node: int, left: int, right: int, ql: int, qr: int) -> int:
        if ql <= left and right <= qr:
            return self.min_val[node]

        mid = left + ((right - left) // 2)
        # Just a large number to set bounds
        answer = 10**18
        if ql <= mid:
            answer = min(answer, self.queryMin(node * 2, left, mid, ql, qr))
        if qr > mid:
            answer = min(answer, self.queryMin(node * 2 + 1, mid + 1, right, ql, qr))

        return answer


class Solution:
    # Segment tree and priority queue
    # Build all the ranges going to the end starting from a left point
    # Then take off pq each max. Every time you do, shrink the right by one and re add
    # Since growing left by 1 is already effectively in queue
    # Time O((n+k)logn)
    # Space O(n)
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Create a segment tree from the numbers
        seg = SegTree(nums)

        # Create priority queue of full length subarray incrementing left
        # Negating just because it's min heap
        pq = [
            (
                -(
                    seg.queryMax(1, 0, n - 1, left, n - 1)
                    - seg.queryMin(1, 0, n - 1, left, n - 1)
                ),
                left,
                n - 1,
            )
            for left in range(n)
        ]
        heapify(pq)

        answer = 0
        while k:
            neg_val, left, right = heappop(pq)
            # This is just adding the subarray value
            answer -= neg_val
            k -= 1
            # Shrink the right hand side by one and add the new subarray
            if right > left:
                heappush(
                    pq,
                    (
                        -(
                            seg.queryMax(1, 0, n - 1, left, right - 1)
                            - seg.queryMin(1, 0, n - 1, left, right - 1)
                        ),
                        left,
                        right - 1,
                    ),
                )

        return answer

test_cases = [
    [4, [1,3,2], 2],
    [12, [4,3,5,1], 3]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxTotalValue(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
