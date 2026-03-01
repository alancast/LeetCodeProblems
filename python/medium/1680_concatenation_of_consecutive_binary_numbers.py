class Solution:
    # Silly math problem
    # Time O(n)
    # Space O(1)
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7

        # Bit length of what's being added
        length = 0
        answer = 0
        for i in range(1, n + 1):
            # When a power of 2, increase the bit length
            if i & (i - 1) == 0:
                length += 1

            # Shift and then add the new number
            answer = ((answer << length) | i) % MOD

        return answer

test_cases = [
    [1, 1],
    [27, 3],
    [505379714, 12]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.concatenatedBinary(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
