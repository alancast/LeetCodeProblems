from typing import List


class Solution:
    # Time O(n) as we go through array once
    # Space O(1)
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Iterate over differences, find min and max
        # Hidden sequence must span max - min
        # Number of sequences is difference - span (+1)
        running_sum = running_max = running_min = 0
        for difference in differences:
            running_sum += difference
            running_max = max(running_max, running_sum)
            running_min = min(running_min, running_sum)

        span = running_max - running_min

        return max(0, upper - lower - span + 1)
    
test_cases = [
    [2, [1,-3,4], 1, 6],
    [4, [3,-4,5,1,-2], -4, 5],
    [0, [4,-7,2], 3, 6],
    [0, [-1,-2,-3], 3, 6],
    [4, [-1,-2,-3], 0, 9],
    [0, [1,2,3], 3, 6],
    [4, [1,2,3], 0, 9]
]
solution = Solution()
for expected, differences, lower, upper in test_cases:
    actual = solution.numberOfArrays(differences, lower, upper)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: differences: {differences}, lower: {lower}, upper: {upper}")

print("Ran all tests")