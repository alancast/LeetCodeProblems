class Solution:
    # Just keep top 2 digits
    # Time O(logn)
    # Space O(1)
    def maxProduct(self, n: int) -> int:
        top_one, top_two = 0, 0

        # Keep shrinking n until it's 0 then do math
        while n > 0:
            rem = n % 10
            if rem > top_one:
                top_one, top_two = rem, top_one
            elif rem > top_two:
                top_two = rem
            n //= 10

        return top_one * top_two

test_cases = [
    [3, 31],
    [4, 22],
    [8, 124]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.maxProduct(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
