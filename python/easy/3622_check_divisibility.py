class Solution:
    # Compute them then do mod
    # Time O(logn)
    # Space O(1)
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        n_copy = n

        while n_copy > 0:
            digit = n_copy % 10
            digit_sum += digit
            digit_product *= digit
            n_copy //= 10

        return n % (digit_product + digit_sum) == 0

test_cases = [
    [True, 99],
    [False, 23]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.checkDivisibility(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
