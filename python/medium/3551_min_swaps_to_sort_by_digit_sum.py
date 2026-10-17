class Solution:
    # Union find
    # Time O(n log n)
    # Space O(n)
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        digitSum = [0] * n
        for i, v in enumerate(nums):
            s = 0
            while v > 0:
                s += v % 10
                v //= 10  # noqa: PLW2901
            digitSum[i] = s

        indices = list(range(n))
        indices.sort(key=lambda i: (digitSum[i], nums[i]))

        targetPos = [0] * n
        for pos, idx in enumerate(indices):
            targetPos[idx] = pos

        parent = list(range(n))
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            ri = find(i)
            rj = find(targetPos[i])
            if ri != rj:
                parent[ri] = rj
                components -= 1

        return n - components

test_cases = [
    [1, [37,100]],
    [0, [22,14,33,7]],
    [2, [18,43,34,16]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minSwaps(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
