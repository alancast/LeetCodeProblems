from collections import defaultdict


class Solution:
    # Go over string once and hashmap char counts
    # Time O(n)
    # Space O(26)
    def maxFreqSum(self, s: str) -> int:
        char_counts = defaultdict(int)
        max_vowel = max_cons = 0

        for char in s:
            char_counts[char] += 1
            if char in "aeiou":
                max_vowel = max(max_vowel, char_counts[char])
            else:
                max_cons = max(max_cons, char_counts[char])

        return max_vowel + max_cons

test_cases = [
    [6, "successes"],
    [3, "aeiaeia"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.maxFreqSum(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")