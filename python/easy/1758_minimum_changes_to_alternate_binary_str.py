class Solution:
    # Go over string once and count hypotheticals in each direction
    # Time O(n)
    # Space O(1)
    def minOperations(self, s: str) -> int:
        # Number of swaps for each
        start_with_zero = start_with_one = 0

        for i, char in enumerate(s):
            # Odd char
            if i & 1:
                if char == '0':
                    start_with_zero += 1
                else:
                    start_with_one += 1
            # Even char
            else:  # noqa: PLR5501
                if char == '1':
                    start_with_zero += 1
                else:
                    start_with_one += 1

        return min(start_with_zero, start_with_one)

test_cases = [
    [1, "0100"],
    [0, "10"],
    [2, "1111"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.minOperations(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
