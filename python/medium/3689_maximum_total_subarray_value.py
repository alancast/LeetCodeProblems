class Solution:
    # Just a simple max - min * k
    # Time O(n)
    # Space O(1)
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        max_num = -1
        min_num = 10000000000

        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        return (max_num - min_num) * k

test_cases = [
    [4, [1,3,2], 2],
    [12, [4,3,5,1], 3]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.maxTotalValue(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
