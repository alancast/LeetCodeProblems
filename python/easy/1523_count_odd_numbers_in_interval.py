class Solution:
    # Just math
    # Time O(1)
    # Space O(1)
    def countOdds(self, low: int, high: int) -> int:
        answer = (high - low) // 2
        # Make sure we count the ends
        if low % 2 == 1 or high % 2 == 1:
            answer += 1

        return answer

test_cases = [
    [3, 3, 7],
    [1, 8, 10],
    [2, 7, 10]
]
solution = Solution()
for expected, low, high in test_cases:
    actual = solution.countOdds(low, high)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: low: {low}, high: {high}")

print("Ran all tests")
