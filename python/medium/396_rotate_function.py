class Solution:
    # Math out the problem
    # Time O(n)
    # Space O(1)
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        f = num_sum = 0

        # Go over all nums and compute sum and find f(0)
        for i, num in enumerate(nums):
            f += i * num
            num_sum += num

        # Go over all possible ranges of f(k) and see which one is max
        answer = f
        for i in range(n - 1, 0, -1):
            f = f + num_sum - n * nums[i]
            answer = max(answer, f)

        return answer

test_cases = [
    [26, [4,3,2,6]],
    [0, [100]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxRotateFunction(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
