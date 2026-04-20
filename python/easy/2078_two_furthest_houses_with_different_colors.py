class Solution:
    # Try going from beginning to find first different color of end
    # And go from end to find first different color from start
    # Take max
    # Time O(n)
    # Space O(1)
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        answer = 0

        # Go from beginning
        end_color = colors[-1]
        for i in range(n):
            if colors[i] != end_color:
                answer = max(answer, n - i - 1)
                break

        # Go from end
        start_color = colors[0]
        for i in range(n-1, -1, -1):
            if colors[i] != start_color:
                answer = max(answer, i)
                break

        return answer

test_cases = [
    [3, [1,1,1,6,1,1,1]],
    [4, [1,8,3,8,3]],
    [1, [0,1]]
]
solution = Solution()
for expected, colors in test_cases:
    actual = solution.maxDistance(colors)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: colors: {colors}")

print("Ran all tests")
