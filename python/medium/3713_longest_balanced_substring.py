from collections import defaultdict


class Solution:
    # Just enumerate all start and end positions
    # Time O(n^2)
    # Space O(n)
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        answer = 0

        # Go over all start points
        for start in range(n):
            # See if we can break out early due to not beating answer
            if n - start <= answer:
                break

            # Reset counts dict
            counts = defaultdict(int)

            # Go over all endings until end and see if balanced
            for end in range(start, n):
                counts[s[end]] += 1

                # See if all chars have same count
                if len(set(counts.values())) == 1:
                    answer = max(answer, end - start + 1)

        return answer

test_cases = [
    [4, "abbac"],
    [4, "zzabccy"],
    [2, "aba"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.longestBalanced(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
