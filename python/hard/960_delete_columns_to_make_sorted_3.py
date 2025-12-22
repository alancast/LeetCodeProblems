from typing import List


class Solution:
    # See how many we can keep and do inverse of that
    # Time O(n * w^2) where w is len of words and n is num words
    # Space O(w)
    def minDeletionSize(self, strs: List[str]) -> int:
        # Find len of all words
        w = len(strs[0])
        dp = [1] * w

        # Go from second to last letter down to first
        # See if all strs are valid if that letter is kept
        # If not increment count and go
        for i in range(w-2, -1, -1):
            # Pick end index
            for j in range(i+1, w):
                # See if these two chars are sorted in all strs
                if all(row[i] <= row[j] for row in strs):
                    # This char can be kept
                    dp[i] = max(dp[i], 1 + dp[j])

        # Answer is total minus max combination of what can be kept
        return w - max(dp)

test_cases = [
    [3, ["babca","bbazb"]],
    [4, ["edcba"]],
    [0, ["ghi","def","abc"]]
]
solution = Solution()
for expected, strs in test_cases:
    actual = solution.minDeletionSize(strs)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: strs: {strs}")

print("Ran all tests")
