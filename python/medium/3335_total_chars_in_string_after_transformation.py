class Solution:
    MOD = 10**9 + 7

    # Math
    # Time O(n + t) get count of each char and then iterate
    # Space O(1) store two 26 int lists
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # Initialize char count array
        char_count = [0] * 26
        for ch in s:
            char_count[ord(ch) - ord('a')] += 1

        # Go through every transformation and create new char counts
        for round in range(t):
            nxt = [0] * 26
            # Create A and B from Z (and A)
            nxt[0] = char_count[25]
            nxt[1] = (char_count[25] + char_count[0]) % self.MOD

            # Take care of the rest of the chars
            for i in range(2, 26):
                nxt[i] = char_count[i - 1]

            char_count = nxt

        return sum(char_count) % self.MOD
    
test_cases = [
    [7, "abcyy", 2],
    [5, "azbk", 1],
    [79033769, "jqktcurgdvlibczdsvnsg", 7517]
]
solution = Solution()
for expected, s, t in test_cases:
    actual = solution.lengthAfterTransformations(s, t)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, t: {t}")

print("Ran all tests")