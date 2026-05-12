class Solution:
    # Another kinda silly problem
    # Dynamic programming
    # DP keeps state of numbers, just need state of num//10 and num % 10 to compute
    # Time O(n)
    # Space O(n)
    def rotatedDigits(self, n: int) -> int:
        # DP has 3 states 0: invalid 1: valid and same 2: valid and change
        # Invalid = has 3,4,7
        # Valid and same = only 0, 1, 8
        # Valid and changed = counts as a GOOD number
        dp = [0] * (n + 1)
        answer = 0

        # Go over all numbers and see if good
        for i in range(n + 1):
            # Set for first 10 numbers
            if i < 10:  # noqa: PLR2004
                if i in (0, 1, 8):
                    dp[i] = 1
                elif i in (2, 5, 6, 9):
                    dp[i] = 2
                    answer += 1
                else:
                    dp[i] = 0
            # Go over previous numbers and see what adding this digit does
            else:
                a = dp[i // 10]
                b = dp[i % 10]

                # Not a good number because doesn't change when rotated
                if a == 1 and b == 1:
                    dp[i] = 1
                # A good number because it changes (know at least one is 2)
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    answer += 1
                # If either is 0 then number is bad
                else:
                    dp[i] = 0

        return answer

test_cases = [
    [4, 10],
    [0, 1],
    [1,2]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.rotatedDigits(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
