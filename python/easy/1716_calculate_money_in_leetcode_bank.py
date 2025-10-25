class Solution:
    # Just do math
    # Time O(1)
    # Space O(1)
    def totalMoney(self, n: int) -> int:
        # Get value for all weeks except for final week
        full_weeks = n // 7
        first_week = 28
        last_week = 28 + (full_weeks - 1) * 7
        arithmetic_sum = (full_weeks * (first_week + last_week)) // 2
        
        # Do final week by self
        monday = 1 + full_weeks
        final_week = 0
        for day in range(n % 7):
            final_week += monday + day
        
        return arithmetic_sum + final_week

test_cases = [
    [10, 4],
    [37, 10],
    [96, 20]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.totalMoney(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
