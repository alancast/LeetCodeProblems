class Solution:
    # Sorting and DP solution
    # Time O(nlogn)
    # Space O(n)
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = {}
        answer = 0

        # Go over all nums and for each num, check if we can take it or not
        for num in nums:
            dp[num + 1] = max(dp.get(num + 1, 0), dp.get(num, 0) + 1)
            dp[num] = max(dp.get(num, 0), dp.get(num - 1, 0) + 1)
            answer = max(answer, dp[num], dp[num + 1])

        return answer

test_cases = [
    [3, [2, 1, 5, 1, 1]],
    [1, [1, 4, 7, 10]],
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxSelectedElements(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}")

print("Ran all tests")
