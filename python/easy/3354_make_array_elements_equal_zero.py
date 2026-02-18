class Solution:
    # Use prefix sum basically
    # total to left and right of digit must be within 1
    # So if we see a 0 check if that's the case, if not continue
    # Time O(n)
    # Space O(1)
    def countValidSelections(self, nums: list[int]) -> int:
        answer = 0
        right = sum(nums)
        left = 0

        # Go over all nums and check if valid for all 0's
        for num in nums:
            if num == 0:
                # Check if within 1 (each direction is a different valid spot)
                if 0 <= left - right <= 1:
                    answer += 1
                if 0 <= right - left <= 1:
                    answer += 1
            # Update sums on each side
            else:
                left += num
                right -= num

        return answer

test_cases = [
    [2, [1,0,2,0,3]],
    [2, [1,0,1]],
    [0, [2,3,4,0,4,1,0]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.countValidSelections(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
