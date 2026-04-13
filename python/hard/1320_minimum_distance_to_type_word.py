class Solution:
    # Time O(n)
    # Space O(n)
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2**30
        dp = [[0] * 26] + [[BIG] * 26 for _ in range(n - 1)]

        def getDistance(p: int, q: int) -> int:
            x1 = p // 6
            y1 = p % 6
            x2 = q // 6
            y2 = q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        # Go over all letters in word
        for i in range(1, n):
            curr = ord(word[i]) - 65
            prev = ord(word[i - 1]) - 65
            d = getDistance(prev, curr)
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
                # The same letter back to back
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, curr)
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + d0)

        return min(dp[n - 1])

test_cases = [
    [3, "CAKE"],
    [6, "HAPPY"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.minimumDistance(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")
