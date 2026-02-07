class Solution:
    # Go over string once and keep track of how many b's
    # As well as how many deletions needed to string up til now to be balanced
    # Optimized DP basically
    # Time O(n)
    # Space O(1)
    def minimumDeletions(self, s: str) -> int:
        answer = 0
        b_count = 0

        # Optimized DP solution where we keep track of how many deletions
        # Needed to make string up til now balanced, then at each char evaluate
        for ch in s:
            if ch == "b":
                b_count += 1
            # If we see an a either remove it from prev balanced string
            # Or remove all the b's
            else:
                answer = min(answer + 1, b_count)

        return answer

test_cases = [
    [2, "aababbab"],
    [2, "bbaaaaabb"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.minimumDeletions(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
