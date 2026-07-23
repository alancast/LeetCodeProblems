class Solution:
    # There is a pattern. So just see that and get answer. Not a good problem
    # Time O(logn)
    # Space O(1)
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:  # noqa: PLR2004
            return n

        answer = 1
        while answer <= n:
            answer <<= 1

        return answer

test_cases = [
    [2, [1,2]],
    [4, [3,1,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.uniqueXorTriplets(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
