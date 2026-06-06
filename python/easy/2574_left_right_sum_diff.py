class Solution:
    # Go over array twice and sum
    # Time O(n)
    # Space O(1)
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        # Find total sum
        total = sum(nums)

        # Build answer by using running sum
        answer = []
        running_sum = 0
        for num in nums:
            right_sum = total - running_sum - num
            answer.append(abs(running_sum - right_sum))
            running_sum += num

        return answer

test_cases = [
    [[15,1,11,22], [10,4,8,3]],
    [[0], [1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.leftRightDifference(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
