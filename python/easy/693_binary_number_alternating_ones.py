class Solution:
    # Divide by 2 each time and see if it equals last
    # Time O(1) as at most 32 divisions
    # Space O(1)
    def hasAlternatingBits(self, n: int) -> bool:
        n, prev_mod = divmod(n, 2)

        # Go until n is 0
        while n:
            # If last num last bit was same as this num then not alternating
            if prev_mod == n % 2:
                return False

            n, prev_mod = divmod(n, 2)

        # Made it to 0 with pure alternating bits so return True
        return True

test_cases = [
    [True, 5],
    [False, 7],
    [False, 11]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.hasAlternatingBits(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
