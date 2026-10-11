class Solution:
    # A special element is at index i if n is divisible by i+1.
    # We only check divisors of n, and use both i and n // i as matching pairs.
    # Time O(sqrt(n))
    # Space O(1)
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0
        i = 1

        while i * i <= n:
            if n % i == 0:
                # Index i-1 is a special element, so include its square.
                answer += nums[i - 1] * nums[i - 1]

                # If i and n // i are different divisors, include the paired element too.
                if i * i != n:
                    answer += nums[n // i - 1] ** 2
            i += 1

        return answer

test_cases = [
    [21, [1, 2, 3, 4]],
    [63, [2, 7, 1, 19, 18, 3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.sumOfSquares(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
