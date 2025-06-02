class Solution:
    # Problem is math
    # Time O(1)
    # Space O(1)
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        # Total number of distributions
        answer += self._cal(n+2)
        # Subtract at least one child receives more than limit
        answer -= (3 * self._cal(n - limit + 1))
        # Re-add two children receive more than limit because they were subtracted twice above
        answer += (3 * self._cal(n - (limit + 1) * 2 + 2))
        # Re-Subtract all three children receive more than limit because they were added above
        answer -= self._cal(n - 3 * (limit + 1) + 2)

        return answer
    
    # Calculate combinations
    def _cal(self, x: int) -> int:
        if x < 0:
            return 0
        return x * (x - 1) // 2
    
test_cases = [
    [3, 5, 2],
    [10, 3, 3]
]
solution = Solution()
for expected, n, limit in test_cases:
    actual = solution.distributeCandies(n, limit)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, limit: {limit}")

print("Ran all tests")