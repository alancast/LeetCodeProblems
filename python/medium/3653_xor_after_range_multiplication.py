class Solution:
    MOD = 10**9 + 7

    # Really stupid problem. Just go over all queries and modify num
    # Time O(nq)
    # Space O(1)
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        # Go over all queries and modify nums in range
        for left, right, k, v in queries:
            for i in range(left, right + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        # Compute the xor
        answer = 0
        for num in nums:
            answer ^= num

        return answer

test_cases = [
    [4, [1,1,1], [[0,2,1,4]]],
    [31, [2,3,1,5,4], [[1,4,2,3], [0,2,1,2]]]
]
solution = Solution()
for expected, nums, queries in test_cases:
    actual = solution.xorAfterQueries(nums, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, queries: {queries}")

print("Ran all tests")
