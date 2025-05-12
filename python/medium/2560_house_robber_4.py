from typing import List


class Solution:
    # Time O(n logn) as log n for search and n for type
    # Space O(1)
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = min(nums)
        right = max(nums)

        # Do binary search to find smallest number we can have be max
        answer = right
        while left <= right:
            mid = (left + right) // 2

            # See if it's possible to rob this many houses
            possible_thefts = 0
            index = 0
            while index < n:
                if nums[index] <= mid:
                    possible_thefts += 1
                    # skip next house. Also can be greedy as it will still be right
                    index += 2
                else:
                    index += 1

            if possible_thefts >= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
            
test_cases = [
    [5, [2,3,5,9], 2],
    [2, [2,7,9,3,1], 2],
    [5, [7,3,9,5], 2],
    [9, [2,7,9,3,1], 3]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.minCapability(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")