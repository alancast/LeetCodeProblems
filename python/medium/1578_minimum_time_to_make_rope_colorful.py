from typing import List


class Solution:
    # Go over colors once, as soon as a color shows up twice in a row
    # Greedily remove whichever is the min of the combo
    # Time O(n)
    # Space O(1)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        prev_kept_idx = 0
        answer = 0
        for i in range(1, n):
            # Same color so remove one
            if colors[i] == colors[prev_kept_idx]:
                # Remove the older one
                if neededTime[prev_kept_idx] <= neededTime[i]:
                    answer += neededTime[prev_kept_idx]
                    prev_kept_idx = i
                # Remove this one
                else:
                    answer += neededTime[i]
            # Different color so this one is kept
            else:
                prev_kept_idx = i

        return answer

test_cases = [
    [3, "abaac", [1,2,3,4,5]],
    [0, "abc", [1,2,3]],
    [2, "aabaa", [1,2,3,4,1]],
    [6, "aaaa", [4,3,2,1]]
]
solution = Solution()
for expected, colors, needed_time in test_cases:
    actual = solution.minCost(colors, needed_time)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: colors: {colors}, needed_time: {needed_time}")

print("Ran all tests")