class Solution:
    # Use a stack to store values and propagate answer
    # Time O(n)
    # Space O(n)
    def maxValue(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n
        # [value, left, right]
        stack = []

        # Go from left to right over stack finding left nums
        for i, num in enumerate(nums):
            curr_val = num
            curr_left = i

            # Figure out biggest number left of this
            while stack and stack[-1][0] > num:
                top_val, top_left, _ = stack.pop()
                curr_val = max(curr_val, top_val)
                curr_left = top_left

            stack.append((curr_val, curr_left, i))

        # Fill in answer from stack
        for i in range(len(stack)):
            # Fill this num from left index to right
            for j in range(stack[i][1], stack[i][2] + 1):
                answer[j] = stack[i][0]

        return answer

test_cases = [
    [[2,2,3], [2,1,3]],
    [[3,3,3], [2,3,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxValue(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
