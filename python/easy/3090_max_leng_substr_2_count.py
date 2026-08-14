from collections import defaultdict


class Solution:
    # Sliding window with counter
    # Time O(n)
    # Space O(n)
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        char_counts = defaultdict(int)
        start = 0
        answer = 0

        for end in range(n):
            char = s[end]
            char_counts[char] += 1

            # Remove from start while too many of this char
            while char_counts[char] > 2:  # noqa: PLR2004
                char_counts[s[start]] -= 1
                start += 1

            answer = max(answer, end - start + 1)

        return answer

test_cases = [
    [4, "bcbbbcba"],
    [2, "aaaa"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.maximumLengthSubstring(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
