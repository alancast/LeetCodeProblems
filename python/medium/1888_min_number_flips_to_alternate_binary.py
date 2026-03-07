class Solution:
    # Added a second type of operation, a rotation.
    # Time O(n)
    # Space O(n)
    def minFlips(self, s: str) -> int:
        # Characteristic function
        def indicator(ch: str, x: int) -> int:
            return int(ord(ch) - ord("0") == x)

        n = len(s)
        pre = [[0, 0] for _ in range(n)]
        # Note the boundary case when i=0
        for i in range(n):
            pre[i][0] = (0 if i == 0 else pre[i - 1][1]) + indicator(s[i], 1)
            pre[i][1] = (0 if i == 0 else pre[i - 1][0]) + indicator(s[i], 0)

        answer = min(pre[n - 1][0], pre[n - 1][1])
        if n % 2 == 1:
            # If n is an odd number, it is also necessary to calculate suf
            suf = [[0, 0] for _ in range(n)]
            # Note the boundary case when i = n - 1
            for i in range(n - 1, -1, -1):
                suf[i][0] = (0 if i == n - 1 else suf[i + 1][1]) + indicator(s[i], 1)
                suf[i][1] = (0 if i == n - 1 else suf[i + 1][0]) + indicator(s[i], 0)

            for i in range(n - 1):
                answer = min(answer, pre[i][0] + suf[i + 1][0])
                answer = min(answer, pre[i][1] + suf[i + 1][1])

        return answer

test_cases = [
    [2, "111000"],
    [0, "010"],
    [1, "1110"],
    [1, "0100"],
    [0, "10"],
    [2, "1111"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.minFlips(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
