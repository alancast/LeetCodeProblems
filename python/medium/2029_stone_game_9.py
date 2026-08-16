class Solution:
    # Could also just do a sum mod 3 but this is better for large sums
    # Stupid problem
    # Time O(n)
    # Space O(1)
    def stoneGameIX(self, stones: list[int]) -> bool:
        rem_0 = rem_1 = rem_2 = 0

        # See how many of each type (remainder 1, 2, 3)
        for val in stones:
            if (rem := val % 3) == 0:
                rem_0 += 1
            elif rem == 1:
                rem_1 += 1
            else:
                rem_2 += 1

        # Just math about what options are left
        if rem_0 % 2 == 0:
            return rem_1 >= 1 and rem_2 >= 1

        return rem_1 - rem_2 > 2 or rem_2 - rem_1 > 2  # noqa: PLR2004

test_cases = [
    [True, [2,1]],
    [False, [2]],
    [False, [5,1,2,4,3]]
]
solution = Solution()
for expected, stones in test_cases:
    actual = solution.stoneGameIX(stones)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: stones: {stones}")

print("Ran all tests")
