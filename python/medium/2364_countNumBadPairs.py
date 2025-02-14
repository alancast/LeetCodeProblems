from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        return self.__count_bad_pairs_count_good(nums)

    # Total pairs = n(n-1)/2. Subtract good pairs
    # Time O(n) Space O(n)
    def __count_bad_pairs_count_good(self, nums: List[int]) -> int:
        bad_pairs = (len(nums) * (len(nums) - 1)) // 2
        good_pairs = 0

        # j - i != nums[j] - nums[i] is the same as nums[j] - j != nums[i] - i
        # So keep track of those diffs in a dict and every time you find one that's a good pair keep track
        # Then compute number of good pairs
        good_diffs = defaultdict(int)
        for i in range(len(nums)):
            diff = nums[i] - i
            if diff in good_diffs:
                good_diffs[diff] += 1
            else:
                good_diffs[diff] = 1

        for value in good_diffs.values():
            good_pairs += (value * (value - 1)) // 2

        return bad_pairs - good_pairs

    # Brute force n^2 calculations
    # Time O(n^2) Space O(1)
    def __count_bad_pairs_brute_force(self, nums: List[int]) -> int:
        bad_pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] != j - i:
                    bad_pairs += 1

        return bad_pairs

testCases = [
    [[1,2,3], 0],
    [[1,3,5,7], 6],
    [[1,2,3,5,7], 7]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.countBadPairs(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Inputs: {nums}")

print("Ran all tests")