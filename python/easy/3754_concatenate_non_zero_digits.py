class Solution:
    # Go digit by digit, create num and add sum then do math at end
    # Time O(logn) log base 10
    # Space O(1)
    def sumAndMultiply(self, n: int) -> int:
        x = sum = 0
        pow10 = 1

        # Go til num is 0 and update numbers we care about
        while n > 0:
            digit = n % 10
            sum += digit

            # Only care if digit is non-zero
            if digit > 0:
                x += digit * pow10
                pow10 *= 10

            # Shrink n down a power of 10
            n //= 10

        return x * sum

test_cases = [
    [12340, 10203004],
    [1, 1000]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.sumAndMultiply(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
