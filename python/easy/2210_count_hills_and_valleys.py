class Solution:
    # Two pointer approach to make sure left and right aren't same as middle
    # And check if middle is hill or valley
    # Time O(n) as we go over the array once
    # Space O(1)
    def countHillValley(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0
        left = 0

        # Go over all nums except for first and last
        for i in range(1, n - 1):
            # If number to right isn't equal to this check if it's a hill or valley
            # If number is equal keep left the same and just go to next number as right
            if nums[i] != nums[i + 1]:
                # Check for a valley
                if nums[i] < nums[left] and nums[i] < nums[i + 1]:
                    answer += 1
                # Check for a hill
                if nums[i] > nums[left] and nums[i] > nums[i + 1]:
                    answer += 1

                # Move left forward to this new num
                left = i

        return answer

test_cases = [
    [3, [2,4,1,1,6,5]],
    [0, [6,6,5,5,4,1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.countHillValley(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
