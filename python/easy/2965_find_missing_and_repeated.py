from typing import List

class Solution:
    # Time O(n^2) as need to read through the whole grid
    # Space O(1)
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = pow(len(grid), 2)
        # Expected sum: n(n+1)/2, Expected square sum: n(n+1)(2n+1)/6
        expected_sum = n * (n + 1) // 2
        expected_square_sum = n * (n + 1) * (2 * n + 1) // 6
        
        sum = square_sum = 0
        # Calculate actual sums from grid
        for row in grid:
            for num in row:
                sum += num
                square_sum += (num * num)
                


        # Calculate differences from expected sums
        sum_diff = sum - expected_sum
        sqr_diff = square_sum - expected_square_sum

        # Using math: If x is repeated and y is missing
        # sum_diff = x - y
        # sqr_diff = x² - y²
        repeat = (sqr_diff // sum_diff + sum_diff) // 2
        missing = (sqr_diff // sum_diff - sum_diff) // 2

        return [repeat, missing]
    
    # Time O(n^2) as need to read through the whole grid
    # Space O(n^2) as might need to store every entry as well
    def findMissingAndRepeatedValues_normal(self, grid: List[List[int]]) -> List[int]:
        # Can find the missing number just by math once we know the dup
        # The grid should sum to n(n+1)/2 so we just need to know the sum and what is done twice
        n = pow(len(grid), 2)
        expected_sum = n * (n+1) // 2
        duplicated_num = sum = 0
        seen = set()
        for row in grid:
            for num in row:
                sum += num
                if num in seen:
                    duplicated_num = num
                    seen.clear()
                    continue
                if duplicated_num != 0:
                    continue

                seen.add(num)

        missing_num = expected_sum - (sum - duplicated_num)
        return [duplicated_num, missing_num]
    
test_cases = [
    [[2,4], [[1,3],[2,2]]],
    [[9,5], [[9,1,7],[8,9,2],[3,4,6]]]
]
solution = Solution()
for expected, grid in test_cases:
    actual = solution.findMissingAndRepeatedValues(grid)
    if expected != actual:
        print(f"FAILED TEST: expected {expected} but got {actual}. INPUTS: grid: {grid}")

print("Ran all tests")