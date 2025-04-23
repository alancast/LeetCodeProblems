from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        self._validate_input
        return self._count_largest_group_math_and_counter(n)
    
    # Time O(n) as we go over each number in n once
    # Space O(n) as we keep array of sums
    def _count_largest_group_math_and_counter(self, n: int) -> int:
        digit_sum = max_count = num_largest = 0

        # Get count of digit sums up til n
        sum_counts = defaultdict(int)
        for i in range(1, n+1):
            digit_sum += 1
            if i % 10000 == 0:
                digit_sum -= 9
            if i % 1000 == 0:
                digit_sum -= 9
            if i % 100 == 0:
                digit_sum -= 9
            if i % 10 == 0:
                digit_sum -= 9

            sum_counts[digit_sum] += 1
            if sum_counts[digit_sum] > max_count:
                max_count = sum_counts[digit_sum]
                num_largest = 1
            elif sum_counts[digit_sum] == max_count:
                num_largest += 1

        return num_largest

    def _validate_input(self, n: int) -> None:
        if n < 1 or n > pow(10,4):
            raise ValueError("n must be between 1 and 10,000")
    
test_cases = [
    [4, 13],
    [9, 9],
    [9, 19],
    [2, 2]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.countLargestGroup(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")