class Solution:
    # Just do math
    # Time O(1)
    # Space O(1)
    def countCommas(self, n: int) -> int:
        if n < 1000:  # noqa: PLR2004
            return 0
        # Every number in this range has one comma so just subtract first 999
        if n < 1000000:  # noqa: PLR2004
            return n - 999

        # Bounds make this the last return amount
        # First 100k have some amount, next all have 2 commas
        return (1000000 - 999) + ((n - 999999) * 2)

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
