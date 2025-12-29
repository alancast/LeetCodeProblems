from typing import List


class Solution:
    # Compute running sum and do comparisons
    # Time O(n)
    # Space O(1)
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)

        points = 0
        running_sum = 0
        # Compute running sum of first k
        for i in range(k):
            running_sum += calories[i]

        # See if first k subarray is points worthy
        if running_sum < lower:
            points -= 1
        if running_sum > upper:
            points += 1

        # Check all k len subarrays to see points
        for i in range(k, n):
            # Add new one and roll out last one
            running_sum -= calories[i-k]
            running_sum += calories[i]
            
            # See if this k subarray is points worthy
            if running_sum < lower:
                points -= 1
            if running_sum > upper:
                points += 1
        
        return points

test_cases = [
    [0, [1,2,3,4,5], 1, 3, 3],
    [1, [3,2], 2, 0, 1],
    [0, [6,5,0,0], 2, 1, 5]
]
solution = Solution()
for expected, calories, k, lower, upper in test_cases:
    actual = solution.dietPlanPerformance(calories, k, lower, upper)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: calories: {calories}, k: {k}, lower: {lower}, upper: {upper}")

print("Ran all tests")