from typing import List


class Solution:
    # Go over list once with a pointer for right and left
    # Time O(n)
    # Space O(1)
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            answer = max(answer, min(height[left], height[right]) * width)

            # Move pointer based on which side is shorter
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return answer

test_cases = [
    [49, [1,8,6,2,5,4,8,3,7]],
    [1, [1,1]],
    [4, [1,2,4,3]]
]
solution = Solution()
for expected, heights in test_cases:
    actual = solution.maxArea(heights)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: heights: {heights}")

print("Ran all tests")
