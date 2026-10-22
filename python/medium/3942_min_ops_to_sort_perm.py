class Solution:
    # Check whether the circular array is a rotated increasing or decreasing sequence.
    # Time O(n)
    # Space O(1)
    def minOperations(self, nums: list[int]) -> int:
        # The array is a cycle, so the first zero marks the rotation start.
        n = len(nums)
        if n == 1:
            return 0

        start = nums.index(0)

        # Track whether the values still match either valid pattern.
        asc = True
        desc = True

        # Walk the circular order from the zero position.
        for i in range(1, n):
            value = nums[(start + i) % n]

            # The ascending pattern expects 1, 2, 3, ... around the ring.
            if value != i:
                asc = False
            # The descending pattern expects n-1, n-2, ... around the ring.
            if value != n - i:
                desc = False

            # If neither pattern still fits, the array cannot be fixed.
            if not asc and not desc:
                return -1

        # If the sequence is in ascending order, return the smaller rotation cost.
        if asc:
            return min(start, n - start + 2)

        # Otherwise it must match the descending order and we use the other rotation cost.
        return min(n - start, start + 2)

test_cases = [
    [2, [0,2,1]],
    [2, [1,0,2]],
    [-1, [2,0,1,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minOperations(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
