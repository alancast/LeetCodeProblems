class Solution:
    # Time O(n) as we go over array once
    # Space O(n) as we could potentially be making a full copy of the array
    def minOperations(self, nums: list[int], k: int) -> int:
        # If k is >= min, it's impossible
        # Otherwise it's a count of the distinct numbers > k
        distinct_nums = set()
        for num in nums:
            if num < k:
                return -1

            if num == k:
                continue

            distinct_nums.add(num)

        return len(distinct_nums)

test_cases = [
    [2, [5,2,5,4,5], 2],
    [0, [2,2,2], 2],
    [-1, [2,1,2], 2],
    [-1, [4,1,6], 3],
    [4, [9,7,5,3], 1]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.minOperations(nums, k)
    if actual != expected:
        print(f"FAILED TEST: Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
