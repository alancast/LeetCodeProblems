class Solution:
    # If the and number anded with negative itself isn't the number then it's not 2
    # Can prove it by doing the bitwise twos compliment
    # Time O(1)
    # Space O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        # No negative number can be power of 2
        if n <= 0:
            return False

        return n & (-n) == n

test_cases = [
    [True, 1],
    [True, 16],
    [False, 3]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.isPowerOfTwo(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
