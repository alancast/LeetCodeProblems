class Solution:
    # Double the subsequences by appending the current character to each one
    # Subtract subsequences that were already created by its previous occurrence
    # Time O(n)
    # Space O(n)
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        subsequences = [1]
        last_seen = {}

        # Include the empty subsequence in the count while building each prefix
        for index, char in enumerate(s):
            current_count = subsequences[-1] * 2
            if char in last_seen:
                # Remove sequences that would be duplicated from this character
                current_count -= subsequences[last_seen[char]]

            subsequences.append(current_count % mod)
            last_seen[char] = index

        # Exclude the empty subsequence from the final result
        return (subsequences[-1] - 1) % mod

test_cases = [
    [7, "abc"],
    [6, "aba"],
    [3, "aaa"],
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.distinctSubseqII(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}")

print("Ran all tests")
