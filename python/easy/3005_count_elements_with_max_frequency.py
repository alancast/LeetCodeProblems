from collections import Counter


class Solution:
    # Time O(n) (could be done in one pass without use of counter but eh)
    # Space O(n)
    def maxFrequencyElements(self, nums: list[int]) -> int:
        num_counts = Counter(nums)
        answer = max_count = 0

        for count in num_counts.values():
            if count < max_count:
                continue

            if count > max_count:
                max_count = count
                answer = count
                continue

            if count == max_count:
                answer += count

        return answer

test_cases = [
    [4, [1,2,2,3,1,4]],
    [5, [1,2,3,4,5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxFrequencyElements(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
