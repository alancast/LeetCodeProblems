class Solution:
    # Just do math
    # Time O(logn)
    # Space O(1)
    def countCommas(self, n: int) -> int:
        # Every multiple of 1000 adds an extra comma
        p = 1000
        answer = 0

        # Keep adding to answer until we are over it
        while p <= n:
            # How many commas in this range
            answer += n - p + 1
            # Take up one level in commas
            p *= 1000

        return answer

test_cases = [
    [3, 1002],
    [0, 998]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.countCommas(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
